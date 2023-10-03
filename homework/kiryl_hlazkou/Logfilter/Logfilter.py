import os
import argparse
import datetime
import glob
from colorama import Fore, Style

# Define color constants
DATE_COLOR = Fore.YELLOW
TEXT_COLOR = Fore.RED
HEADER_COLOR = Fore.CYAN

# Define the argument parser
parser = argparse.ArgumentParser(description='Log File Filter')

# Add arguments for specifying folder path or search criteria
parser.add_argument('path', help='Folder path containing log files or path to a single log file')
parser.add_argument('--date', help="Datetime for search (format: 'YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--date_less', help="Filter logs less than the specified date (format: 'YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--date_greater', help="Filter logs greater than date (format: 'YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--date_range', help="Filter logs date range ('YYYY-MM-DD HH:MM:SS.fff/YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--text', help='Filter logs by text content')
parser.add_argument('--notext', help='Exclude logs that contain the specified text')
parser.add_argument('--full', help='Display the full log messages', action='store_true')

args = parser.parse_args()


# Function to fetch logs from a file
def fetch_logs(file):
    if os.path.isfile(file):
        with open(file, 'r') as log_file:
            return log_file.read()
    else:
        print(f"Invalid file or folder path: {file}")
        exit()


# Function to extract log blocks and store them in a dictionary
def extract_log_blocks(log_content):
    # Create an empty dictionary to store log blocks with timestamps as keys
    log_blocks = {}

    # Split the log content into individual lines
    lines = log_content.splitlines()

    # Initialize variables to keep track of the current log block and its timestamp
    current_block = []
    current_date = None

    # Iterate through each line in the log content
    for line in lines:
        if line.strip():  # Check if the line is not empty (non-empty lines are part of the log)
            # Attempt to extract a timestamp from the line using the get_timestamp function
            timestamp = get_timestamp(line)

            if timestamp:
                # If a timestamp is found, it indicates the start of a new log entry

                # Check if there was a previous log entry (current_block is not empty)
                if current_date:
                    # If there was a previous log entry, store it in the log_blocks dictionary
                    # using the timestamp (current_date) as the key and join the lines as the value
                    log_blocks[current_date] = '\n'.join(current_block)

                # Update current_date with the newly found timestamp
                current_date = timestamp

                # Initialize a new current_block list with the current line as its first element
                current_block = [line]
            else:
                # If there is no timestamp on the line, it is part of the current log entry
                # Append the line to the current_block list

                current_block.append(line)
        elif current_block:
            # If an empty line is encountered, it marks the end of the current log entry
            # Check if there was a current log entry (current_block is not empty)

            # Store the current log entry in the log_blocks dictionary
            # using the timestamp (current_date) as the key and join the lines as the value
            log_blocks[current_date] = '\n'.join(current_block)

            # Reset current_block and current_date for the next log entry
            current_block = []
            current_date = None

    # Check if there is a remaining log entry after processing all lines
    if current_block and current_date:
        # Store the remaining log entry in the log_blocks dictionary
        log_blocks[current_date] = '\n'.join(current_block)

    # Return the dictionary containing log entries with timestamps as keys
    return log_blocks


# Function to get timestamp from a line
def get_timestamp(line):
    try:
        return datetime.datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        return None


# Function to colorize text within log entries
def colorize_log_entry(log_entry):
    # Colorize the date
    log_entry = log_entry.replace(log_entry[:23], DATE_COLOR + log_entry[:23] + Style.RESET_ALL, 1)

    # Colorize the text (if specified)
    if args.text and args.text in log_entry:
        log_entry = log_entry.replace(args.text, TEXT_COLOR + args.text + Style.RESET_ALL)

    return log_entry


# Function to filter and print log entries based on criteria
def filter_and_print_logs(log_content, arguments):
    log_blocks = extract_log_blocks(log_content)
    matching_logs = {}
    total_logs_count = len(log_blocks)

    for date, block in log_blocks.items():
        if arguments.date:
            target_date = datetime.datetime.strptime(arguments.date, '%Y-%m-%d %H:%M:%S.%f')
            if date != target_date:
                continue

        if arguments.date_less:
            target_date = datetime.datetime.strptime(arguments.date_less, '%Y-%m-%d %H:%M:%S.%f')
            if not (date < target_date):
                continue

        if arguments.date_greater:
            target_date = datetime.datetime.strptime(arguments.date_greater, '%Y-%m-%d %H:%M:%S.%f')
            if not (date > target_date):
                continue

        if arguments.date_range:
            date_range = arguments.date_range.split('/')
            if len(date_range) == 2:
                start_date = datetime.datetime.strptime(date_range[0], '%Y-%m-%d %H:%M:%S.%f')
                end_date = datetime.datetime.strptime(date_range[1], '%Y-%m-%d %H:%M:%S.%f')
                if not (start_date <= date <= end_date):
                    continue

        if arguments.text and arguments.text in block:
            if arguments.notext and arguments.notext in block:
                continue
            matching_logs[date] = block
        elif arguments.text:
            continue
        else:
            if arguments.notext and arguments.notext in block:
                continue
            matching_logs[date] = block

    total_results_count = len(matching_logs)

    # Display log entries in the desired format
    for date, log_entry in matching_logs.items():
        if arguments.full:
            print(colorize_log_entry(log_entry))
        else:
            if arguments.text:
                index = log_entry.find(arguments.text)
                if index != -1:
                    start_index = max(0, index - 150)
                    end_index = min(index + len(arguments.text) + 150, len(log_entry))
                    log_entry = log_entry[start_index:end_index]
            log_entry_short = log_entry[:300]  # Display the first 300 characters
            print(colorize_log_entry(log_entry_short))

    # Apply color to headers and display counts
    print(HEADER_COLOR + f"Total logs count: {total_logs_count}" + Style.RESET_ALL)
    print(HEADER_COLOR + f"Total results count: {total_results_count}" + Style.RESET_ALL)


# Check if the input path is a file or folder
if os.path.isfile(args.path):
    # If it's a single file, process it
    logs_content = fetch_logs(args.path)
    print(f"Processing logs from: {args.path}")
    filter_and_print_logs(logs_content, args)
elif os.path.isdir(args.path):
    # If it's a folder, use glob to find all log files and process them
    log_files = glob.glob(os.path.join(args.path, '*.log'))
    for log in log_files:
        print(f"Processing logs from: {log}")
        logs_content = fetch_logs(log)
        filter_and_print_logs(logs_content, args)
else:
    print("Invalid file or folder path.")
