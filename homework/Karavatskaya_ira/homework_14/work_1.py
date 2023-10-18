import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='magic',
   passwd='AVNS_jkeRJRRrvKwNQzsTAHE',
   database='magic'
)


cursor = db.cursor(dictionary=True)
# Создание группы
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('AQA-01', 'jun-2023', 'des-2024')")
group_id = cursor.lastrowid

# Создание студента
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Martin', 'Lutter', %s)", (group_id,))
student_id = cursor.lastrowid

# Создание книг
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Lutherbibel', %s)", (student_id,))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Philosophy', %s)", (student_id,))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Theology', %s)", (student_id,))

# Обновление группы студента
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

# Создание предметов
cursor.execute("INSERT INTO subjets (title) VALUES ('history')")
cursor.execute("INSERT INTO subjets (title) VALUES ('biology')")
cursor.execute("INSERT INTO subjets (title) VALUES ('math')")

# Создание занятий
cursor.execute("INSERT INTO subjets (title) VALUES ('history')")
cursor.execute("INSERT INTO subjets (title) VALUES ('biology')")
cursor.execute("INSERT INTO subjets (title) VALUES ('math')")

# Создание оценок
lesson_ids = [12, 13, 14, 15, 16, 17]
mark_values = [8, 7, 9, 6, 10, 7]
for lesson_id, value in zip(lesson_ids, mark_values):
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (value, lesson_id, student_id))

# Получение оценок студента
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
print("Оценки студента:", marks)

# Получение названий книг, взятых студентом
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
print("Книги, взятые студентом:", books)

# Получение информации о студенте, группе, книгах и оценках
cursor.execute("""
    SELECT *
    FROM students
    JOIN `groups` ON `groups`.id = students.group_id
    JOIN books ON books.taken_by_student_id = students.id
    JOIN marks ON marks.student_id = students.id
    WHERE students.id = %s
""", (student_id,))
data = cursor.fetchall()
print("Данные студента:", data)

cursor.close()
db.close()
