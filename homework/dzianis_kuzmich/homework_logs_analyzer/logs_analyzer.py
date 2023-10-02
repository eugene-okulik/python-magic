import os
import re
import argparse
from datetime import datetime
from colorama import init, Fore


def get_logs_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def get_logs_from_directory(directory_path):
    logs = ''
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.log'):
            with open(os.path.join(directory_path, file_name), 'r') as f:
                logs += f.read()
    return logs


def extract_blocks(logs):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    messages = re.split(pattern, logs)

    blocks = {}  # Modified
    for i in range(0, len(messages) - 1, 2):
        date = datetime.strptime(messages[i], '%Y-%m-%d %H:%M:%S')
        blocks[date] = messages[i + 1].strip()

    return blocks


def filter_by_date(blocks, start_date=None, end_date=None):
    if start_date:
        blocks = {date: msg for date, msg in blocks.items() if date >= start_date}
    if end_date:
        blocks = {date: msg for date, msg in blocks.items() if date <= end_date}
    return blocks


def filter_by_text(blocks, include_text=None, exclude_text=None):
    if include_text:
        blocks = {date: msg for date, msg in blocks.items() if include_text in msg}
    if exclude_text:
        blocks = {date: msg for date, msg in blocks.items() if exclude_text not in msg}
    return blocks


def print_results(blocks, search_text=None, full_message=False):
    for date, msg in blocks.items():
        if search_text and search_text in msg:
            idx = msg.index(search_text)
            before_txt = msg[max(0, idx-150):idx]  # Modified
            after_txt = msg[idx+len(search_text):idx+len(search_text)+150]  # Modified
            print(Fore.YELLOW + f'[{date}] ' + Fore.WHITE + before_txt
                  + Fore.GREEN + search_text + Fore.WHITE + after_txt)  # Modified
        else:
            print(Fore.YELLOW + f'[{date}] ' + Fore.WHITE + (msg if full_message else msg[:300]))


def main():
    parser = argparse.ArgumentParser(description="Logs Analyzer")
    parser.add_argument("path", help="Path to file or directory with logs.")
    parser.add_argument("--start_date",
                        type=datetime.fromisoformat,
                        help="Filter logs by start date. Format: YYYY-MM-DD")
    parser.add_argument("--end_date", type=datetime.fromisoformat, help="Filter logs by end date. Format: YYYY-MM-DD")
    parser.add_argument("--include_text", help="Filter logs that include the specified text.")
    parser.add_argument("--exclude_text", help="Filter logs that exclude the specified text.")
    parser.add_argument("--full_message", action="store_true", help="Print the full log message.")
    args = parser.parse_args()

    if os.path.isfile(args.path):
        logs = get_logs_from_file(args.path)
    elif os.path.isdir(args.path):
        logs = get_logs_from_directory(args.path)
    else:
        print(Fore.RED + "Invalid path. Please provide a valid file or directory path.")
        return

    blocks = extract_blocks(logs)
    blocks = filter_by_date(blocks, args.start_date, args.end_date)
    blocks = filter_by_text(blocks, args.include_text, args.exclude_text)

    print_results(blocks, args.include_text, args.full_message)


if __name__ == "__main__":
    init(autoreset=True)
    main()
