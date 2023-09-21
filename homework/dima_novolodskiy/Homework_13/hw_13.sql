INSERT INTO students (name, second_name, group_id) VALUES ('Igor', 'Perminov', 3)

INSERT INTO books (title, taken_by_student_id) VALUES ('Math', 36)
INSERT INTO books (title, taken_by_student_id) VALUES ('Philosophy', 36)
INSERT INTO books (title, taken_by_student_id) VALUES ('Biology', 36)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('NDA-141', 'Oct-2023', 'Jun-2024')

UPDATE students SET group_id = 20 WHERE id = 36

INSERT INTO subjets (title) VALUES ('Python')

INSERT INTO subjets (title) VALUES ('SQL')

INSERT INTO subjets (title) VALUES ('K8S')

INSERT INTO lessons (title, subject_id) VALUES ('Lesson_one', 10)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson_two', 10)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson_one', 11)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson_two', 11)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson_one', 12)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson_two', 12)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 18, 36)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('4', 19, 36)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 20, 36)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 21, 36)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('3', 22, 36)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 23, 36)

SELECT value FROM marks WHERE student_id = 36

SELECT title FROM books WHERE taken_by_student_id = 36

SELECT *
FROM students
INNER JOIN `groups` ON students.group_id  = `groups`.id
INNER JOIN books ON students.id  = books.taken_by_student_id
INNER JOIN marks ON students.id = marks.student_id
INNER JOIN lessons ON marks.lesson_id = lessons.id
INNER JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.id = 36

