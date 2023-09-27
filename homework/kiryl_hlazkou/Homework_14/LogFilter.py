import os
import argparse
import datetime
import requests
from urllib.parse import urlparse

# Define the argument parser
parser = argparse.ArgumentParser(description='Log File Filter')

# Add arguments for specifying URL or local file and search criteria
parser.add_argument('url_or_file', help='URL to a log file or local file containing log data')
parser.add_argument('--date', help="Datetime for search (format: 'YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--date_less', help="Filter logs less than the specified date (format: 'YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--date_greater', help="Filter logs greater than  date (format: 'YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--date_range', help="Filter logs date range ('YYYY-MM-DD HH:MM:SS.fff/YYYY-MM-DD HH:MM:SS.fff')")
parser.add_argument('--text', help='Filter logs by text content')
parser.add_argument('--notext', help='Exclude logs that contain the specified text')
parser.add_argument('--full', help='Display the full log messages', action='store_true')

args = parser.parse_args()


# Function to fetch logs from URL or read logs from a local file
def fetch_logs(url_or_file):
    parsed_url = urlparse(url_or_file)

    if parsed_url.scheme in ('http', 'https'):
        try:
            response = requests.get(url_or_file)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs from URL: {e}")
            exit()
    elif os.path.isfile(url_or_file):
        with open(url_or_file, 'r') as log_file:
            return log_file.read()
    else:
        print("Invalid URL or file path.")
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
            print(log_entry)
        else:
            if args.text:
                index = log_entry.find(args.text)
                if index != -1:
                    start_index = max(0, index - 150)
                    end_index = min(index + len(args.text) + 150, len(log_entry))
                    log_entry = log_entry[start_index:end_index]
            log_entry_short = log_entry[:300]  # Display the first 300 characters
            print(log_entry_short)

    print(f"Total logs count: {total_logs_count}")
    print(f"Total results count: {total_results_count}")


# Fetch logs from the provided URL or local file
log_content = fetch_logs(args.url_or_file)

# Process and filter logs
print(f"Processing logs from: {args.url_or_file}")
filter_and_print_logs(log_content, args)
