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
    log_blocks = {}
    lines = log_content.splitlines()
    current_block = []
    current_date = None

    for line in lines:
        if line.strip():  # Check if the line is not empty
            timestamp = get_timestamp(line)
            if timestamp:
                if current_date:
                    log_blocks[current_date] = '\n'.join(current_block)
                current_date = timestamp
                current_block = [line]
            else:
                current_block.append(line)
        elif current_block:
            log_blocks[current_date] = '\n'.join(current_block)
            current_block = []
            current_date = None

    # Check if there is a remaining block after processing all lines
    if current_block and current_date:
        log_blocks[current_date] = '\n'.join(current_block)

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
def filter_and_print_logs(log_content, args):
    log_blocks = extract_log_blocks(log_content)
    matching_logs = {}
    total_logs_count = len(log_blocks)

    for date, block in log_blocks.items():
        if args.date:
            target_date = datetime.datetime.strptime(args.date, '%Y-%m-%d %H:%M:%S.%f')
            if date != target_date:
                continue

        if args.date_less:
            target_date = datetime.datetime.strptime(args.date_less, '%Y-%m-%d %H:%M:%S.%f')
            if not (date < target_date):
                continue

        if args.date_greater:
            target_date = datetime.datetime.strptime(args.date_greater, '%Y-%m-%d %H:%M:%S.%f')
            if not (date > target_date):
                continue

        if args.date_range:
            date_range = args.date_range.split('/')
            if len(date_range) == 2:
                start_date = datetime.datetime.strptime(date_range[0], '%Y-%m-%d %H:%M:%S.%f')
                end_date = datetime.datetime.strptime(date_range[1], '%Y-%m-%d %H:%M:%S.%f')
                if not (start_date <= date <= end_date):
                    continue

        if args.text and args.text in block:
            if args.notext and args.notext in block:
                continue
            matching_logs[date] = block
        elif args.text:
            continue
        else:
            if args.notext and args.notext in block:
                continue
            matching_logs[date] = block

    total_results_count = len(matching_logs)

    # Display log entries in the desired format
    for date, log_entry in matching_logs.items():
        if args.full:
            print(colorize_log_entry(log_entry))
        else:
            log_entry_short = log_entry[:300]  # Display the first 300 characters
            print(colorize_log_entry(log_entry_short))

    # Apply color to headers and display counts
    print(HEADER_COLOR + f"Total logs count: {total_logs_count}" + Style.RESET_ALL)
    print(HEADER_COLOR + f"Total results count: {total_results_count}" + Style.RESET_ALL)


# Check if the input path is a file or folder
if os.path.isfile(args.path):
    # If it's a single file, process it
    log_content = fetch_logs(args.path)
    print(f"Processing logs from: {args.path}")
    filter_and_print_logs(log_content, args)
elif os.path.isdir(args.path):
    # If it's a folder, use glob to find all log files and process them
    log_files = glob.glob(os.path.join(args.path, '*.log'))
    for log_file in log_files:
        print(f"Processing logs from: {log_file}")
        log_content = fetch_logs(log_file)
        filter_and_print_logs(log_content, args)
else:
    print("Invalid file or folder path.")
