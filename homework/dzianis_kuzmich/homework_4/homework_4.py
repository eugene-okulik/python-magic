# Task 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# Task 2

strings = ["результат операции: 42", "результат операции: 54"]

for s in strings:
    colon_index = s.index(':')
    number = int(s[colon_index + 2:])
    result = number + 10
    print(result)

# Task 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

text = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"
print(text)
