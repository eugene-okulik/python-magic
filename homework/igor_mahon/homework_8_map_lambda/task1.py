# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
#
# Преобразуйте эту дату в питоновский формат, после этого распечатайте полное название месяца из этой даты
#
# Распечатайте дату в таком формате: "15.01.2023, 12:05"

from datetime import datetime

python_date = datetime.strptime("Jan 15, 2023 - 12:05:33", "%b %d, %Y - %X")

print(python_date.strftime("%B"))

print(python_date.strftime("%d.%m.%Y, %H:%M"))
