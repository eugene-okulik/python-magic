import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='magic',
    passwd='AVNS_jkeRJRRrvKwNQzsTAHE',
    database='magic'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Bary', 'Ruby', 1)")
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Arts_new', 20)")
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Math_new', 20)")
db.commit()
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('TSR-17', 'Dec-2023', 'Mar-2026')")
db.commit()
cursor.execute("UPDATE students SET group_id = 17 WHERE id = 20")
db.commit()
cursor.execute("INSERT INTO subjets  (title) VALUES ('ARTS')")
db.commit()
cursor.execute("INSERT INTO subjets (title) VALUES ('SIENCE')")
db.commit()
cursor.execute("INSERT INTO subjets (title) VALUES ('ENGLISH')")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('first_lesson', 2)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('second_lesson', 2)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('first_lesson', 3)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('second_lesson', 3)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('first_lesson', 4)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('second_lesson', 4)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 2, 20)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 3, 20)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('B+', 4, 20)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('A+', 5, 20)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('C-', 6, 20)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('B+', 7, 20)")
db.commit()


cursor.execute("SELECT value FROM marks WHERE student_id = 20")
print(cursor.fetchall())

cursor.execute("SELECT title FROM books WHERE taken_by_student_id = 20")
print(cursor.fetchall())

cursor.execute('''
SELECT * FROM students
join `groups`
ON `groups`.id = students.group_id
join books
ON books.taken_by_student_id = students.id 
join marks
ON marks.student_id = students.id
WHERE students.id = 20
''')
print(cursor.fetchall())

db.close()
