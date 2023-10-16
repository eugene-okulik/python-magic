import mysql.connector as mysql
import credentials as creds  # create a credentials.py where all creds are stored

db = mysql.connect(
    host=creds.host,
    port=creds.port,
    user=creds.user,
    password=creds.passwd,
    database=creds.database
)

cursor = db.cursor(dictionary=True)
# Создайте студента (student)
cursor.execute("INSERT INTO magic.students (name, second_name) VALUES ('Dave', 'Mustaine')")
# store id of a new record in a variable
new_student_id = cursor.lastrowid

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
cursor.execute("INSERT INTO magic.books (title, taken_by_student_id) VALUES ('Angry again', %s)", (new_student_id, ))
new_book_1 = cursor.lastrowid
cursor.execute("INSERT INTO magic.books (title, taken_by_student_id) VALUES ('Peace Sells', %s)", (new_student_id, ))
new_book_2 = cursor.lastrowid

# Создайте группу (group)
cursor.execute("INSERT INTO magic.groups (title, start_date, end_date) VALUES ('Megadeath', 'Oct-1983', 'Oct-2083')")
new_group = cursor.lastrowid

# и определите своего студента туда
cursor.execute("UPDATE magic.students SET group_id = %s WHERE id = %s", (new_group, new_student_id))

# Создайте несколько учебных предметов (subjects)
cursor.execute("INSERT INTO magic.subjets (title) VALUES ('Orchestra')")
new_subject_1 = cursor.lastrowid
cursor.execute("INSERT INTO magic.subjets (title) VALUES ('Chorus')")
new_subject_2 = cursor.lastrowid

# Создайте по два занятия для каждого предмета (lessons)
cursor.execute("INSERT INTO magic.lessons (title, subject_id) VALUES ('1 Lesson', %s)", (new_subject_1, ))
new_lesson_1 = cursor.lastrowid
cursor.execute("INSERT INTO magic.lessons (title, subject_id) VALUES ('2 Lesson', %s)", (new_subject_1, ))
new_lesson_2 = cursor.lastrowid
cursor.execute("INSERT INTO magic.lessons (title, subject_id) VALUES ('1 Lesson', %s)", (new_subject_2, ))
new_lesson_3 = cursor.lastrowid
cursor.execute("INSERT INTO magic.lessons (title, subject_id) VALUES ('2 Lesson', %s)", (new_subject_2, ))
new_lesson_4 = cursor.lastrowid

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
cursor.execute(
    "INSERT INTO magic.marks (value, lesson_id, student_id) VALUES ('Good', %s, %s)", (new_lesson_1, new_student_id)
)
cursor.execute(
    "INSERT INTO magic.marks (value, lesson_id, student_id) VALUES ('Good', %s, %s)", (new_lesson_2, new_student_id)
)
cursor.execute(
    "INSERT INTO magic.marks (value, lesson_id, student_id) VALUES ('Good', %s, %s)", (new_lesson_3, new_student_id)
)
cursor.execute(
    "INSERT INTO magic.marks (value, lesson_id, student_id) VALUES ('Good', %s, %s)", (new_lesson_4, new_student_id)
)

# Получите информацию из базы данных:
# Все оценки студента
cursor.execute("SELECT value Marks FROM magic.marks WHERE student_id = %s", (new_student_id, ))
print(cursor.fetchall())

# Все книги, которые находятся у студента
cursor.execute("SELECT title FROM magic.books WHERE taken_by_student_id = %s", (new_student_id, ))
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
query = '''
SELECT gr.title GROUPNAME, st.name FIRSTNAME, st.second_name SECONDNAME, b.title BOOKTITLE, m.value MARK, l.title LESSON
FROM magic.groups gr
JOIN magic.students st
ON gr.id = st.group_id
JOIN magic.books b
ON b.taken_by_student_id = st.id
JOIN magic.marks m
ON m.student_id = st.id
JOIN magic.lessons l
ON m.lesson_id = l.id
WHERE st.id = %s
'''
cursor.execute(query, (new_student_id, ))
print(cursor.fetchall())

# commit all changes to the DB
db.commit()
db.close()
