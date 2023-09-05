import datetime


date_str = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

print("Полное название месяца:", python_date.strftime('%B'))

formatted_date_str = python_date.strftime("%d.%m.%Y, %H:%M")
print("Форматированная дата:", formatted_date_str)
