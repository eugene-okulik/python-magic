import os
import sys
import argparse  # The argparse module makes it easy to write user-friendly command-line interfaces.
from datetime import datetime
# Improve the appearance of executing in the terminal/cmd ;)
from colorama import Fore, init, just_fix_windows_console
just_fix_windows_console()
init(autoreset=True)


# The first step in using the argparse is creating an ArgumentParser object:
parser = argparse.ArgumentParser(
    prog="'LogZilla' by Igor Mahon. \nPlease put log file/s in the path: ...python-magic/homework/eugene_okulik/data\n",
    description="Find info in logs according to the given parameters. " +
                "By default it prints the first 300 symbols of the log.",
    epilog="!All rights reserved!")

# Filling ArgumentParser with information about program arguments is done by making calls to the add_argument() method.
parser.add_argument("file", help="path to file/directory")
parser.add_argument("-dt", "--datetime", help='datetime to search: ' +
                                              'to date: "../2023-01-01 00:00:00.000", ' +
                                              'from date: "2023-01-01 00:00:00.000/..", ' +
                                              'from-to date: "2023-01-01 00:00:00.000|2023-01-01 00:00:00.000", ' +
                                              'exact date: "=2023-01-01 00:00:00.000".')
parser.add_argument("-t", "--text", help="text to search")
parser.add_argument("-e", "--exclude", help="text to exclude from search")
parser.add_argument("-f", "--full", help="return full log instead of default symbols QTy(300 by default)",
                    action="store_true")
args = parser.parse_args()
print(Fore.CYAN + "\nYou've entered these parameters:")
print(f"Filename: {args.file}" +
      f"\nDatetime to search: {args.datetime}" +
      f"\nText to search: {args.text}" +
      f"\nText to exclude from search: {args.exclude}" +
      f"\nDisplay the full log: {args.full}"
      )
print(Fore.LIGHTBLACK_EX + '*****************************************************************************************')

# find the directory with the file
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
log_path = os.path.join(homework_path, 'homework', 'eugene_okulik', 'data/logs', args.file)
# log_path = os.path.join(homework_path, 'homework', 'igor_mahon', args.file)


# determine what the user specified: a file or a folder.
def determine_file_or_folder(path):
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'is a folder not a file'
    else:
        return "The path doesn't exist. "


# Check and forewarned user if the file is not specified
if determine_file_or_folder(log_path) != 'file':
    print(Fore.BLUE + determine_file_or_folder(log_path) + Fore.RED +
          "Please enter the file name placed in the path: ...python-magic/homework/eugene_okulik/data/FILE_NAME.log")
    sys.exit()

# Read the file
with open(log_path, 'r') as file:
    initial_logs = file.read()

# Create a new dictionary where a datetime object(timestamp) is a key, the rest is a value
log_dict = {}
lines = initial_logs.strip().split('\n')
# Counter of logs in the file/s
count_logs = 0
for line in lines:
    # The '2' parameter passed to the split() function indicates that the splitting should happen only two times.
    parts = line.split(' ', 2)
    # The parts list contains three elements: the date, the time, and the rest of the line after the timestamp.
    timestamp = ' '.join(parts[:2]).strip()
    # The size of the timestamp is always 23 chars :)
    if len(timestamp) != 23:
        continue
    # Convert timestamp to datetime object
    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
    print(timestamp)
    log_dict[timestamp] = parts[2]
    count_logs += 1
print("==========================")
print(str(log_dict)[:200])
print("Count_logs", count_logs)


def datetime_converter_searcher(log_dictionary, datetime_to_search):
    if datetime_to_search is None:
        return None
    elif datetime_to_search[:3] == '../' and len(datetime_to_search) == 26:  # to: ../2023-01-01 00:00:00.000
        search_to = datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if logDatetime <= search_to:
                search_results[logDatetime] = logText
        # return <class 'datetime.datetime'> or None if search_results = {}
        return search_results or None

    elif datetime_to_search[-3:] == '/..' and len(datetime_to_search) == 26:  # from: 2023-01-01 00:00:00.000/..
        search_from = datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if logDatetime >= search_from:
                search_results[logDatetime] = logText
        # return <class 'datetime.datetime'> or None if search_results = {}
        return search_results or None

    elif datetime_to_search[:1] == '=' and len(datetime_to_search) == 24:  # exact: =2023-01-01 00:00:00.000
        search_exact = datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if logDatetime == search_exact:
                search_results[logDatetime] = logText
        # return <class 'datetime.datetime'> or None if search_results = {}
        return search_results or None

    # from-to: 2023-01-01 00:00:00.000|2023-01-01 00:00:00.000
    elif datetime_to_search[23:-23] == '|' and len(datetime_to_search) == 47:
        datetime_from, datetime_to = datetime_to_search.split('|')
        search_from_to = (
            datetime.strptime(datetime_from, "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime(datetime_to, "%Y-%m-%d %H:%M:%S.%f")
        )
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if search_from_to[0] <= logDatetime <= search_from_to[1]:
                search_results[logDatetime] = logText
        # return <class 'datetime.datetime'> or None if search_results = {}
        return search_results or None


def search_by_text(log_dictionary1, search_text=None, exclude_text=None):
    search_results = {}
    for log_datetime, log_text in log_dictionary1.items():
        # Convert all strings to lowercase for ease of search
        log_text_lower = log_text.lower()

        if search_text is not None and exclude_text is not None:
            # Both search_text and exclude_text provided
            if search_text.lower() in log_text_lower and exclude_text.lower() not in log_text_lower:
                search_results[log_datetime] = log_text
        elif search_text is not None:
            # Only search_text provided
            if search_text.lower() in log_text_lower:
                search_results[log_datetime] = log_text
        elif exclude_text is not None:
            # Only exclude_text provided
            if exclude_text.lower() not in log_text_lower:
                search_results[log_datetime] = log_text
    return search_results or None


# Perform the datetime search only if dates is not None
if args.datetime is not None:
    datetime_results = datetime_converter_searcher(log_dict, args.datetime)
else:
    datetime_results = None

# Perform the text search only if texts is not None
if args.text is not None or args.exclude is not None:
    text_results = search_by_text(log_dict, args.text, args.exclude)
else:
    text_results = None

# Initialize an empty dictionary to store the filtered results
filtered_results = {}

# Check which filter was applied and populate filtered_results accordingly
if datetime_results and text_results:
    # Both datetime and text filters are applied
    for log_datetime, log_text in datetime_results.items():
        if log_datetime in text_results:
            filtered_results[log_datetime] = log_text
elif datetime_results:
    # Only datetime filter is applied
    filtered_results = datetime_results
elif text_results:
    # Only text filter is applied
    filtered_results = text_results

if filtered_results:
    # Initialize an empty dictionary and populate it with a for loop
    result_dict = {}
    for log_datetime, log_text in filtered_results.items():
            result_dict[str(log_datetime)] = log_text
else:
    print("No matching entries found.")

print(Fore.GREEN + 'Please see results:')
print(str(result_dict)[:300])
print(Fore.LIGHTBLACK_EX + "*****************************************************************************************")
print("Total number of logs that were handled:", count_logs)
print("The number of logs that meet search criteria:", len(result_dict))

sys.exit(Fore.LIGHTRED_EX + '\nThanks for using!')
