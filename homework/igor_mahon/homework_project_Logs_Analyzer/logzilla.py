import os
import sys
import argparse  # The argparse module makes it easy to write user-friendly command-line interfaces.
from datetime import datetime
from colorama import Fore, init, just_fix_windows_console  # Improve the appearance of executing in the terminal/cmd ;)
just_fix_windows_console()  # Improve the appearance of executing in the terminal/cmd ;)
init(autoreset=True)  # Improve the appearance of executing in the terminal/cmd ;)


# The first step in using the argparse is creating an ArgumentParser object:
parser = argparse.ArgumentParser(
    prog="'LogZilla' by Igor Mahon. \nPlease put log file/s in the path: ...python-magic/homework/eugene_okulik/data\n",
    description="Find info in logs according to the given parameters. " +
                "By default it prints the first 300 symbols of the log.",
    epilog="!All rights reserved!")

# Filling an ArgumentParser with information about program arguments is done
# by making calls to the add_argument() method.
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


# check and forewarned user if the file is not specified
if determine_file_or_folder(log_path) != 'file':
    print(Fore.BLUE + determine_file_or_folder(log_path) + Fore.RED +
          "Please enter the file name placed in the path: ...python-magic/homework/eugene_okulik/data/FILE_NAME.log")
    sys.exit()

# read the file
with open(log_path, 'r') as file:
    initial_logs = file.read()

# Create a new dict where datetime object is a key, the rest is a value
# FYI The dictionary in Python does not allow to duplicate keys!
log_dict = {}
lines = initial_logs.strip().split('\n')
# Counter of logs in the file/s
count_logs = 0
for line in lines:
    # The '2' parameter passed to the split() function indicates that the splitting should happen only two times.
    parts = line.split(' ', 2)
    # The parts list contains three elements: the date, the time, and the rest of the line after the timestamp.
    timestamp = ' '.join(parts[:2]).strip()
    # The size of the timestamp is always 23 chars and the 10 element is 'whitespace'
    if len(timestamp) != 23:
        continue
    # Convert timestamp to datetime object
    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
    timestamp_str = str(timestamp)[:-3]
    print(timestamp, timestamp_str)
    log_dict[timestamp_str] = parts[2]
    # Convert timestamp to string
    # timestamp_str = str(timestamp)
    # print(timestamp_str)
    # log_dict[timestamp_str].append(parts[2])
    # if timestamp_str in log_dict:
    #     log_dict[timestamp_str].append(parts[2])
    # else:
    #     log_dict[timestamp_str] = [parts[2]]
    count_logs += 1
    # string_dict = str(log_dict)
    # print(string_dict[:100])
print("==========================")
print(str(log_dict)[:200])
print("Count_logs", count_logs)
# # Create a new dict where datetime object is a key, the rest is a value
# # FYI The dictionary in Python does not allow to duplicate keys!
# log_dict = {}
# # Counter of logs in the file/s
# count_logs = 0
# # Split logs to lines by \n
# lines = initial_logs.split('\n')
# for line in lines:
#     # For each non-empty line, the script splits it by spaces
#     if line.strip() != '':
#         parts = line.split(' ')
#         # Skip if the parts list does not have enough elements
#         if len(parts) < 2:
#             continue
#         date_str = parts[0] + ' ' + parts[1]
#         message = ' '.join(parts[2:])
#         # Skip if the datetime string is empty
#         if date_str.strip() == '':
#             continue
#         try:
#             date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
#             log_dict[date] = message
#         except ValueError:
#             print(f"Invalid date format: {date_str}")
#             continue
#     count_logs += 1
# print("Count_logs", count_logs)


# # Parser of the datetime input according to the -h(help description)
# def datetime_parser(datetime_to_search):
#     if datetime_to_search is None:
#         pass
#     elif datetime_to_search.startswith('../') and datetime_to_search is not None:
#         # to: ../2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'>
#         return datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
#     elif datetime_to_search.endswith('/..') and datetime_to_search is not None:
#         # to: 2023-01-01 00:00:00.000/..
#         # return <class 'datetime.datetime'>
#         return datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
#     elif datetime_to_search.startswith('-'):
#         # exact: -2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'>
#         return datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
#     elif '|' in datetime_to_search and datetime_to_search is not None:
#         # from-to: 2023-01-01 00:00:00.000|2023-01-01 00:00:00.000
#         datetime_from, datetime_to = datetime_to_search.split('|')
#         # return tuple
#         return (
#             datetime.strptime(datetime_from, "%Y-%m-%d %H:%M:%S.%f"),
#             datetime.strptime(datetime_to, "%Y-%m-%d %H:%M:%S.%f")
#         )
#
#
# # Search by datetime
# def search_by_datetime(dict1, search_dates):
#     if search_dates is None:
#         return None
#     # check if the search_dates variable is an instance of the datetime class using isinstance()
#     elif isinstance(search_dates, datetime):
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime == search_dates:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     # check if the search_dates variable is a tuple with two elements to handle 'from - to' search
#     elif isinstance(search_dates, tuple) and len(search_dates) == 2:
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if search_dates[0] <= log_datetime <= search_dates[1]:
#                 search_results.append((log_datetime, log_text))
#         return search_results


# def datetime_converter_searcher(dict1, datetime_to_search):
#     # do nothing if the user did not enter value - > return None
#     if datetime_to_search is None:
#         return None
#     # add check if isinstance(datetime_to_search, datetime):
#     elif '../' in datetime_to_search:
#         # convert to: ../2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'>
#         search_to = datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
#         # search result by 'date to'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime <= search_to:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     elif '/..' in datetime_to_search:
#         # convert from: 2023-01-01 00:00:00.000/..
#         # return <class 'datetime.datetime'>
#         search_from = datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
#         # search result by 'date from'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime >= search_from:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     elif '=' in datetime_to_search:
#         # convert exact: =2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'>
#         search_exact = datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
#         # search result by 'exact date'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime == search_exact:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     elif '|' in datetime_to_search:
#         datetime_from, datetime_to = datetime_to_search.split('|')
#         # convert from-to: 2023-01-01 00:00:00.000|2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'> as tuple
#         search_from_to = (
#             datetime.strptime(datetime_from, "%Y-%m-%d %H:%M:%S.%f"),
#             datetime.strptime(datetime_to, "%Y-%m-%d %H:%M:%S.%f")
#         )
#         # search result by 'from-to date'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if search_from_to[0] <= log_datetime <= search_from_to[1]:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#
#
# print("=========datetime")
# test = datetime_converter_searcher(log_dict, args.datetime)  # for debugging
# print(str(test)[:100])  # for debugging
# print(type(test))  # for debugging
# #
#
# # Search by text
# def search_by_text(dict1, search_text, exclude_text):
#     if search_text is None:
#         return None
#     search_results = []
#     for log_datetime, log_text in dict1.items():
#         if search_text in log_text and (exclude_text is None or exclude_text not in log_text):
#             search_results.append((log_datetime, log_text))
#     return search_results
#
#
# print("=========text")
# test2 = search_by_text(log_dict, args.text, args.exclude)  # for debugging
# print(str(test2)[:100])  # for debugging
# print(type(test2))  # for debugging


# # Search by datetime and text
# def search_by_datetime_and_text(dict1, search_dates, search_text, exclude_text, full):
#     datetime_results = datetime_converter_searcher(dict1, search_dates)
#     text_results = search_by_text(dict1, search_text, exclude_text)
#     if datetime_results is None and text_results is None:
#         return sys.exit('Nothing to search :(')
#     elif datetime_results is None:
#         if full:
#             return [f"{str(log_datetime)}, {str(log_text)}" for log_datetime, log_text in text_results]
#         else:
#             return [f"{str(log_datetime)}, {str(log_text)[:300]}" for log_datetime, log_text in text_results]
#     elif text_results is None:
#         if full:
#             return [f"{str(log_datetime)}, {str(log_text)}" for log_datetime, log_text in datetime_results]
#         else:
#             return [f"{str(log_datetime)}, {str(log_text)[:150]}" for log_datetime, log_text in datetime_results]
#     combined_results = []
#     for datetime_result, log_text in datetime_results:
#         if datetime_result in text_results:
#             combined_results.append((datetime_result, log_text))
#     if full:
#         return [f"{str(log_datetime)}, {str(log_text)}" for log_datetime, log_text in combined_results]
#     else:
#         return [f"{str(log_datetime)}, {str(log_text)[:150]}" for log_datetime, log_text in combined_results]
#
#
# print(Fore.GREEN + 'Please see results:')
# result = search_by_datetime_and_text(log_dict, datetime_converter_searcher(log_dict, args.datetime), args.text, args.exclude, args.full)
# print(str(result).strip('[]'))
# print(Fore.LIGHTBLACK_EX + "*****************************************************************************************")
# print("Total number of logs that were handled:", count_logs)
# print("The number of logs that meet search criteria:", len(result))
#
# sys.exit(Fore.LIGHTRED_EX + '\nThanks for using!')
