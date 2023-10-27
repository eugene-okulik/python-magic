
import random

import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='magic',
    passwd='AVNS_jkeRJRRrvKwNQzsTAHE',
    database='magic'
)
cursor = db.cursor(dictionary=True)

name, second_name, group_name = input('Enter name, last name and group number: ').split()
query = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
values = (name, second_name, group_name)
cursor.execute(query, values)
id_student = cursor.lastrowid
db.commit()

number_of_books = int(input('Enter number of books: '))
for update in range(number_of_books):
    title = input(f'Enter title book №{update + 1}: ')
    query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
    values = (title, id_student)
    cursor.execute(query, values)
    db.commit()

title_group, start_date, end_date = input('Enter title grop, start date and end date: ').split()
query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values = (title_group, start_date, end_date)
cursor.execute(query, values)
id_grop = cursor.lastrowid
db.commit()


cursor.execute(f"UPDATE students SET group_id = {id_grop} WHERE id = {id_student}")
db.commit()

list_subjects = input('Enter the name of the subjects you want to add: ').split()
id_subjects = []
for subject in list_subjects:
    query = 'INSERT INTO subjets (title) VALUES (%s)'
    values = (subject,)
    cursor.execute(query, values)
    id_subjects.append(cursor.lastrowid)
    db.commit()

lst_lesson = []
for subject_id in id_subjects:
    query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
    values = ('Lesson_one', subject_id)
    cursor.execute(query, values)
    lst_lesson.append(cursor.lastrowid)
    query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
    values = ('Lesson_two', subject_id)
    cursor.execute(query, values)
    lst_lesson.append(cursor.lastrowid)
    db.commit()


query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
for id_lesson in lst_lesson:
    values = (str(random.randint(1, 5)), id_lesson, id_student)
    cursor.execute(query, values)
    db.commit()

cursor.execute(f"SELECT value FROM marks WHERE student_id = {id_student}")
print(cursor.fetchall())

cursor.execute(f'SELECT title FROM books WHERE taken_by_student_id = {id_student}')
print(cursor.fetchall())

cursor.execute(f'''
SELECT *
FROM students
INNER JOIN `groups` ON students.group_id  = `groups`.id
INNER JOIN books ON students.id  = books.taken_by_student_id
INNER JOIN marks ON students.id = marks.student_id
INNER JOIN lessons ON marks.lesson_id = lessons.id
INNER JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.id = {id_student}
'''
               )
print(cursor.fetchall())

db.close()
