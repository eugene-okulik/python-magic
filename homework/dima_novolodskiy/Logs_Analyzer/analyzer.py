import os
import argparse
import datetime
from colorama import Fore

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


def list_files(path):
    if os.path.isfile(args.file):
        return [args.file]
    elif os.path.isdir(args.file):
        return [os.path.join(args.file, file) for file in os.listdir(args.file) if file.endswith(".log")]


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
                    dict_logs[word] = ''
                    current_categ = word
                    new_category = False
                else:
                    dict_logs[current_categ] += f' {word}'
    return dict_logs


def date_sort(date, logs):
    dict_sort_date = {}
    if date[0] == '.':
        input_date = datetime.datetime.fromisoformat(f'{date[3:]}')
        for log in logs:
            if datetime.datetime.fromisoformat(log) <= input_date:
                dict_sort_date[log] = logs[log]
    elif date[-1] == '.':
        input_date = datetime.datetime.fromisoformat(f'{date[:-3]}')
        for log in logs:
            if datetime.datetime.fromisoformat(log) >= input_date:
                dict_sort_date[log] = logs[log]
    elif date[0] != '.' and date[-1] != '.' and '/' in date:
        input_date_a, input_date_b = date.split('/')
        input_date_a = datetime.datetime.fromisoformat(input_date_a)
        input_date_b = datetime.datetime.fromisoformat(input_date_b)
        for log in logs:
            if input_date_a <= datetime.datetime.fromisoformat(log) <= input_date_b:
                dict_sort_date[log] = logs[log]
    elif date[0] != '.' and date[-1] != '.' and '/' not in date:
        input_date = datetime.datetime.fromisoformat(date)
        for log in logs:
            if datetime.datetime.fromisoformat(log) == input_date:
                dict_sort_date[log] = logs[log]
    return dict_sort_date


def text_sort(text, dict_logs):
    dict_sort_text = {}
    for log in dict_logs:
        if text in dict_logs[log]:
            dict_sort_text[log] = dict_logs[log]
    return dict_sort_text


def unwanted_sort(unwanted, dict_logs):
    dict_sort_unwanted = {}
    for log in dict_logs:
        if unwanted not in dict_logs[log]:
            dict_sort_unwanted[log] = dict_logs[log]
    return dict_sort_unwanted


def find_word(log, word):
    index = log.find(word)
    b_index = max(0, index - 150)
    a_index = min(len(log), index + len(word) + 150)
    fist_str = log[b_index:index]
    second_str = log[index + len(word):a_index]
    extracted_text = [fist_str, second_str]
    return extracted_text


list_log = list_files(args.file)
total_logs_count = parsing(list_log)
dict_log = parsing(list_log)
if args.date is not None:
    dict_log = date_sort(args.date, dict_log)
if args.text is not None:
    dict_log = text_sort(args.text, dict_log)
if args.unwanted is not None:
    dict_log = unwanted_sort(args.unwanted, dict_log)

if args.text is not None:
    for log in dict_log:
        text_log = find_word(dict_log[log], args.text)
        print(Fore.LIGHTYELLOW_EX + f'[{log}]' + ' ' + Fore.LIGHTWHITE_EX + text_log[
            0] + Fore.LIGHTGREEN_EX + args.text + Fore.LIGHTWHITE_EX + text_log[1])
else:
    if args.full is False:
        for log in dict_log:
            print(
                Fore.LIGHTYELLOW_EX + f'[{log}]' + ' ' + Fore.LIGHTWHITE_EX + f'{dict_log[log][0:300]}')
    else:
        for log in dict_log:
            print(Fore.LIGHTYELLOW_EX + f'[{log}]' + ' ' + Fore.LIGHTWHITE_EX + f'{dict_log[log]}')

print(Fore.LIGHTYELLOW_EX + 'Total logs count:' + Fore.LIGHTCYAN_EX + f' {len(total_logs_count)}')
print(Fore.LIGHTYELLOW_EX + 'Total results count:' + Fore.LIGHTCYAN_EX + f' {len(dict_log)}')
