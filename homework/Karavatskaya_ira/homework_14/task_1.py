import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='magic',
   passwd='AVNS_jkeRJRRrvKwNQzsTAHE',
   database='magic'
)


cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO `groups` (title, start_date,end_date) values ('AQA-01', 'jun-2023', 'des-2024')")
db.commit()
cursor.execute("INSERT INTO students (name, second_name, group_id) values ('Martin', 'Lutter', 11)")
last_id = cursor.lastrowid
db.commit()
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Lutherbibel', {last_id})")
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) values ('Philosophy',  {last_id})")
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) values ('Theology',  {last_id})")
db.commit()
cursor.execute("UPDATE students SET group_id = 11 WHERE id =  {last_id}")
db.commit()
cursor.execute("INSERT INTO subjets (title) VALUES ('history')")
db.commit()
cursor.execute("INSERT INTO subjets (title) VALUES ('biology')")
db.commit()
cursor.execute("INSERT INTO subjets (title) VALUES ('math')")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('classes one', 7)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('classes two', 7)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('classes two', 8)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('classes one', 9)")
db.commit()
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('classes two', 9)")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 12,  {last_id})")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 13,  {last_id})")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 14,  {last_id})")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (6, 15,  {last_id})")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 16,  {last_id})")
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 17,  {last_id})")
db.commit()

cursor.execute("SELECT value FROM marks WHERE student_id =  {last_id}")
print(cursor.fetchall())

cursor.execute("SELECT title FROM books WHERE taken_by_student_id =  {last_id}")
print(cursor.fetchall())

cursor.execute('''
SELECT * FROM students
JOIN `groups`
ON `groups`.id = students.group_id
JOIN books
ON books.taken_by_student_id = students.id
JOIN marks
ON marks.student_id = students.id
WHERE students.id =  {last_id}
''')
print(cursor.fetchall())

db.close()