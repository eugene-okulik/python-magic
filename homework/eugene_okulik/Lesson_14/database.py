import mysql.connector as mysql
import credentials as creds
import os
import dotenv

dotenv.load_dotenv()


db = mysql.connect(
   host=os.getenv('DB_HOST'),
   port=os.getenv('DB_PORT'),
   user=os.getenv('DB_USER'),
   passwd=os.getenv('DB_PASSW'),
   database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM students')
print(cursor.fetchall())
cursor.execute('SELECT * FROM students WHERE id = 6')
print(cursor.fetchone()['name'])
# cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Petr', 'Petrov', 2)")
# print(cursor.lastrowid)
# db.commit()

user_input = input('name and second_name: ')
name, second_name = user_input.split()
# cursor.execute(f"SELECT * FROM students WHERE name = '{name}' and second_name = '{second_name}'")
cursor.execute("SELECT * FROM students WHERE name = %s and second_name = %s", (name, second_name))

print(cursor.fetchall())

query = '''
SELECT * FROM students
JOIN `groups` 
ON `groups`.id = students.group_id
JOIN books
ON books.taken_by_student_id = students.id
JOIN marks
ON marks.student_id = students.id
JOIN lessons
ON lessons.id = marks.lesson_id
WHERE students.id = 23
'''
db.close()
