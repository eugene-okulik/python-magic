import os


def read_logs(folder_path):
    logs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".log"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                logs.extend(file.readlines())
    return logs


def filter_logs(logs, date=None, date_greater=None, date_less=None, text_contains=None, text_not_contains=None):
    filtered_logs = []
    for log in logs:
        log_date = log.split()[0]  # предполагается, что дата находится в начале строки
        log_text = log.split()[1:]  # предполагается, что текст сообщения идет после даты
        if date and log_date != date:
            continue
        if date_greater and log_date <= date_greater:
            continue
        if date_less and log_date >= date_less:
            continue
        if text_contains and text_contains not in log_text:
            continue
        if text_not_contains and text_not_contains in log_text:
            continue
        filtered_logs.append(log)
    return filtered_logs


def print_logs(logs, full_message=False):
    for log in logs:
        if full_message:
            print(log)
        else:
            print(log[:300])


# Пример использования программы
folder_path = input("Введите путь к папке с лог-файлами: ")
logs = read_logs(folder_path)

date = input("Введите дату для фильтрации (YYYY-MM-DD): ")
date_greater = input("Введите дату для фильтрации (больше указанной, YYYY-MM-DD): ")
date_less = input("Введите дату для фильтрации (меньше указанной, YYYY-MM-DD): ")
text_contains = input("Введите текст для фильтрации (поиск по наличию): ")
text_not_contains = input("Введите текст для фильтрации (поиск по отсутствию): ")

filtered_logs = filter_logs(logs, date, date_greater, date_less, text_contains, text_not_contains)
print_logs(filtered_logs, full_message=True)
