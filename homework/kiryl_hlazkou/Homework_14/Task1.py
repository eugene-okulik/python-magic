import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='magic',
    passwd='AVNS_jkeRJRRrvKwNQzsTAHE',
    database='magic'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO subjets (title) VALUES ('Rock')")
db.commit()
cursor.execute("INSERT INTO subjets (title) VALUES ('Funk')")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Introduction', 19)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Introduction', 20)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Practice', 19)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Practice', 20)")
db.commit()
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('KH-01', 'Oct - 2023', 'Nov - 2023')")
db.commit()
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('John', 'Doe', 2)")
db.commit()
new_student_id = cursor.lastrowid
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('RHCP', %s)", (new_student_id,))
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('RATM', %s)", (new_student_id,))
db.commit()
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('KH-01', 'Oct - 2023', 'Nov - 2023')")
db.commit()
cursor.execute("UPDATE students SET group_id = 24 where id = %s", (new_student_id,))
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('Passed', 34, %s)", (new_student_id,))
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('Passed', 35, %s)", (new_student_id,))
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('Failed', 36, %s)", (new_student_id,))
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('Failed', 37, %s)", (new_student_id,))
db.commit()

cursor.execute("SELECT `value` FROM marks WHERE student_id = %s", (new_student_id,))
print(cursor.fetchall())

cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (new_student_id,))
print(cursor.fetchall())

cursor.execute('''
SELECT * FROM students
JOIN `groups`
ON `groups`.id = students.group_id
JOIN books
ON books.taken_by_student_id = students.id
JOIN marks
ON marks.student_id = students.id
JOIN lessons
ON lessons.id = marks.lesson_id
WHERE students.id = %s
''', (new_student_id,))
print(cursor.fetchall())

db.close()
