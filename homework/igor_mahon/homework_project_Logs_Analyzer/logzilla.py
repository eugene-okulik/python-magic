import os
import sys
import argparse  # The argparse module makes it easy to write user-friendly command-line interfaces.
from datetime import datetime
# Improve the appearance of executing in the terminal/cmd ;)
from colorama import Fore, init
init(autoreset=True)

# The first step in using the argparse is creating an ArgumentParser object:
parser = argparse.ArgumentParser(
    prog="\n*************************************************\n" +
         f"{Fore.YELLOW}          'LogZilla' by Igor Mahon.{Fore.RESET}\n" +
         "*************************************************\n",
    description="Find info in logs according to the given parameters. " +
                "By default it prints the first 300 symbols of the log(if [-f]= False)",
    epilog=f"{Fore.BLUE}!All rights reserved!{Fore.RESET}"
)

# Filling ArgumentParser with information about program arguments is done by making calls to the add_argument() method.
parser.add_argument("file", help="path to file/folder. "
                                 "The default path is set to: python-magic/homework/eugene-okulik/data/" +
                                 f"{Fore.RED}[enter path to the file/folder name]{Fore.RESET}"
                    )
parser.add_argument("-dt", "--datetime", help='datetime to search: ' +
                                              'to date: "../2023-01-01 00:00:00.000", ' +
                                              'from date: "2023-01-01 00:00:00.000/..", ' +
                                              'from-to date: "2023-01-01 00:00:00.000|2023-01-01 00:00:00.000", ' +
                                              'exact date: "=2023-01-01 00:00:00.000".'
                    )
parser.add_argument("-t", "--text", help="text to search")
parser.add_argument("-e", "--exclude", help="text to exclude from search")
parser.add_argument("-f", "--full", help="return full log instead of default symbols QTy(300 by default)",
                    action="store_true"
                    )
args = parser.parse_args()
print(Fore.CYAN + "\nYou've entered these parameters:")
print(f"{Fore.LIGHTBLACK_EX}Filename or the path to file/s:{Fore.RESET} {args.file}" +
      f"\n{Fore.LIGHTBLACK_EX}Datetime to search:{Fore.RESET} {args.datetime}" +
      f"\n{Fore.LIGHTBLACK_EX}Text to search:{Fore.RESET} {args.text}" +
      f"\n{Fore.LIGHTBLACK_EX}Text to exclude from search:{Fore.RESET} {args.exclude}" +
      f"\n{Fore.LIGHTBLACK_EX}Display the full log:{Fore.RESET} {args.full}"
      )
print(Fore.LIGHTBLACK_EX + '***********************************************************************')

# Create a root_path for 'python-magic'
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Get user input for the path
log_path = os.path.join(root_path, 'homework', 'eugene_okulik', 'data', args.file)


# Determine whether the user input is a file or folder.
def determine_file_or_folder(path):
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'folder'
    else:
        return 'invalid path'


# Check and forewarn the user if the input is invalid.
input_type = determine_file_or_folder(log_path)
if input_type == 'invalid path':
    print(Fore.RED + "Invalid path. Please enter a valid file or folder path. " +
          "The default path is set to: python-magic/homework/eugene-okulik/data/" +
          f"{Fore.RED}[enter path to the file/folder name]{Fore.RESET}"
          )
    sys.exit()
elif input_type == 'folder':
    print(Fore.BLUE + "You've provided a folder path. Reading all files in the folder...")

# Initialize a dictionary where a datetime object (timestamp) is a key, the rest is a value
log_dict = {}
# Initialize a total counter of logs in a file or in files(in folder)
total_count_logs = 0

# Read the file(s) if it's a valid file or all files in the folder.
if input_type == 'file':
    with open(log_path, 'r') as file:
        initial_logs = file.read()
        lines = initial_logs.strip().split('\n')
        # Output the name of the handled file, need to investigate how :)
        print(f"{Fore.BLUE}Reading one file...{Fore.RESET}")
        for line in lines:
            # The '2' parameter passed to the split() function indicates that the splitting should happen only two times
            parts = line.split(' ', 2)
            # The parts list contains three elements: the date, the time, and the rest of the line after the timestamp.
            timestamp = ' '.join(parts[:2]).strip()
            # The size of the timestamp is always 23 characters :)
            if len(timestamp) != 23:
                continue
            # Convert timestamp to datetime object
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            log_dict[timestamp] = parts[2]
            total_count_logs += 1
else:
    # Read all files in the folder
    for filename in os.listdir(log_path):
        file_path = os.path.join(log_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                initial_logs = file.read()
                # Output the names of all handled files
                print(f"Reading file: {filename}")
                lines = initial_logs.strip().split('\n')
                for line in lines:
                    parts = line.split(' ', 2)
                    timestamp = ' '.join(parts[:2]).strip()
                    if len(timestamp) != 23:
                        continue
                    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
                    log_dict[timestamp] = parts[2]
                    total_count_logs += 1


#  Convert args.datetime to datetime object and then search by datetime in the provided dictionary
def datetime_converter_searcher(log_dictionary, datetime_to_search):
    if datetime_to_search is None:
        return None
    elif datetime_to_search[:3] == '../' and len(datetime_to_search) == 26:  # to: ../2023-01-01 00:00:00.000
        search_to = datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if logDatetime <= search_to:
                search_results[logDatetime] = logText
        # Return <class 'datetime.datetime'> or None if search_results = {}(Empty dictionary)
        return search_results or None

    elif datetime_to_search[-3:] == '/..' and len(datetime_to_search) == 26:  # from: 2023-01-01 00:00:00.000/..
        search_from = datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if logDatetime >= search_from:
                search_results[logDatetime] = logText
        # Return <class 'datetime.datetime'> or None if search_results = {}
        return search_results or None

    elif datetime_to_search[:1] == '=' and len(datetime_to_search) == 24:  # exact: =2023-01-01 00:00:00.000
        search_exact = datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
        search_results = {}
        for logDatetime, logText in log_dictionary.items():
            if logDatetime == search_exact:
                search_results[logDatetime] = logText
        # Return <class 'datetime.datetime'> or None if search_results = {}
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
        # Return <class 'datetime.datetime'> or None if search_results = {}
        return search_results or None


#  Search by text in the dictionary
#
def search_by_text(log_dictionary1, search_text=None, exclude_text=None):
    search_results = {}
    for logDatetime, logText in log_dictionary1.items():
        # Convert all strings to lowercase for ease of search
        log_text_lower = logText.lower()

        if search_text is not None and exclude_text is not None:
            # Both search_text and exclude_text provided
            if search_text.lower() in log_text_lower and exclude_text.lower() not in log_text_lower:
                search_results[logDatetime] = logText
        elif search_text is not None:
            # Only search_text provided
            # This is not implemented - need more time for investigation:
            # "Если производился поиск по тексту (не по отсутствию),
            # то выводить 150 символов до найденного текста, сам текст и 150 символов после текста"
            if search_text.lower() in log_text_lower:
                search_results[logDatetime] = logText
        elif exclude_text is not None:
            # Only exclude_text provided
            if exclude_text.lower() not in log_text_lower:
                search_results[logDatetime] = logText
    return search_results or None


# Processing results of methods search_by_text & datetime_converter_searcher for output to the terminal
# Perform the datetime search only if dates is not None
if args.datetime is not None:
    datetime_results = datetime_converter_searcher(log_dict, args.datetime)
else:
    datetime_results = None

# Perform the text search only if texts or exclude text is not None
if args.text is not None or args.exclude is not None:
    text_results = search_by_text(log_dict, args.text, args.exclude)
else:
    text_results = None

# Initialize an empty dictionary to store the final results
filtered_results = {}

# Check which filter was applied and populate filtered_results accordingly
if datetime_results and text_results:
    # Both datetime and text filters are applied
    for log_datetime, log_text in datetime_results.items():
        if log_datetime in text_results:
            # Check if log_text contains exclude_text and exclude it if it does
            if args.exclude is None or args.exclude.lower() not in log_text.lower():
                filtered_results[log_datetime] = log_text
elif datetime_results:
    # Only datetime filter is applied
    for log_datetime, log_text in datetime_results.items():
        # Check if log_text contains exclude_text and exclude it if it does
        if args.exclude is None or args.exclude.lower() not in log_text.lower():
            filtered_results[log_datetime] = log_text
elif text_results:
    # Only text filter is applied
    for log_datetime, log_text in text_results.items():
        # If the def 'search_by_text' receives two arguments(search_text, exclude_text)
        # that are mutually exclusive(e.g. search_text = "Error", exclude_text"Error"), it returns None.
        # So need another check for exclusion here
        if args.exclude is None or args.exclude.lower() not in log_text.lower():
            filtered_results[log_datetime] = log_text

if filtered_results:
    result_dict = {}
    for log_datetime, log_text in filtered_results.items():
        result_dict[str(log_datetime)] = log_text
    # Here is the final results that are ready for output
    final_dict = dict(result_dict)

    # Output results
    print(Fore.GREEN + 'Please see results:')
    for final_key, final_value in final_dict.items():
        # if args.full = True, return all text
        if args.full:
            print(f"{Fore.RED}{str(final_key)}{Fore.RESET} {final_value}")
        # if args.full = False, return 300 symbols - default value
        else:
            print(f"{Fore.RED}{str(final_key)}{Fore.RESET} {final_value[:300]}...")
    print(
        Fore.LIGHTBLACK_EX + "***********************************************************************"
    )
    print(f"{Fore.YELLOW}Total number of logs that were handled:{total_count_logs}")
    print(f"{Fore.YELLOW}The number of logs that meet search criteria:{len(final_dict)}")
else:
    print("No matching entries found.")

sys.exit(Fore.LIGHTBLUE_EX + '\nThanks for using!')
