import os
import argparse
import datetime
from colorama import Fore, Style

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to file or directory")
parser.add_argument("-d", "--date", help="Datetime for search: less than: '../2022-01-13 00:00:00.000',"
                                         "more than: '2022-01-13 00:00:00.000/..',"
                                         "from - to '2022-01-13 00:00:00.000/2022-01-14 00:00:00.000',"
                                         "exact: '2022-01-13 00:00:00.000'")
parser.add_argument("-t", "--text", help="A text to look for")
parser.add_argument("-n", "--unwanted", help="A text to filter out logs. Logs with this text will be "
                                             "excluded from the results. Can be a string or a list divided by commas "
                                             "(e.g. 'out of memory, info')")
parser.add_argument("--full", help="Return full log entry instead of default symbols Qty",
                    action="store_true")
args = parser.parse_args()


def list_files(files):
    if os.path.isfile(files):
        return [files]
    elif os.path.isdir(files):
        return [os.path.join(files, file) for file in os.listdir(files) if file.endswith(".log")]


def parsing(list_file):
    dict_logs = {}
    for file in list_file:
        with open(file) as new_file:
            lst_file = new_file.read().split()
            for index, keyword in enumerate(lst_file):
                if len(keyword) == 10 and keyword[4] == '-' and keyword[7] == '-':
                    if lst_file[index + 1][2] == ':' and lst_file[index + 1][5] == ':':
                        lst_file[index + 1] = lst_file[index] + ' ' + lst_file[index + 1]
                        lst_file[index] = 'split'
            new_category = True
            current_categ = None
            for word in lst_file:
                if 'split' == word:
                    new_category = True
                    current_categ = None
                    continue
                if new_category:
                    dict_logs[word] = []
                    current_categ = word
                    new_category = False
                else:
                    dict_logs[current_categ].append(word)
    return dict_logs


def date_sort(date, logs):
    dict_sort_date = {}
    if date[0] == '.':
        input_date = datetime.datetime.fromisoformat(f'{date[3:]}')
        for log in logs:
            if datetime.datetime.fromisoformat(log) < input_date:
                dict_sort_date[log] = logs[log]
    elif date[-1] == '.':
        input_date = datetime.datetime.fromisoformat(f'{date[:-3]}')
        for log in logs:
            if datetime.datetime.fromisoformat(log) > input_date:
                dict_sort_date[log] = logs[log]
    elif date[0] != '.' and date[-1] != '.' and '/' in date:
        input_date_a, input_date_b = date.split('/')
        input_date_a = datetime.datetime.fromisoformat(input_date_a)
        input_date_b = datetime.datetime.fromisoformat(input_date_b)
        for log in logs:
            if input_date_a < datetime.datetime.fromisoformat(log) < input_date_b:
                dict_sort_date[log] = logs[log]
    elif date[0] != '.' and date[-1] != '.' and '/' not in date:
        input_date = datetime.datetime.fromisoformat(date)
        for log in logs:
            if datetime.datetime.fromisoformat(log) == input_date:
                dict_sort_date[log] = logs[log]
    return dict_sort_date


if args.file is not None:
    list_log = list_files(args.file)
    dict_log = parsing(list_log)
if args.date is not None:
    sort_date = date_sort(args.date, dict_log)

print(sort_date.keys())
