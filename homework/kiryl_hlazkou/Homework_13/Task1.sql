INSERT INTO students (name, second_name, group_id) VALUES ('Kiryl', 'Hlazkou', 2)
INSERT INTO books (title, taken_by_student_id) VALUES ('RHCP', 42)
INSERT INTO books (title, taken_by_student_id) VALUES ('RATM', 42)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('KH-01', 'Oct - 2023', 'Nov - 2023')
UPDATE students SET group_id = 24 where id = 42
INSERT INTO subjets (title) VALUES ('Rock')
INSERT INTO subjets (title) VALUES ('Funk')
INSERT INTO lessons (title, subject_id) VALUES ('Introduction', 19)
INSERT INTO lessons (title, subject_id) VALUES ('Introduction', 20)
INSERT INTO lessons (title, subject_id) VALUES ('Practice', 19)
INSERT INTO lessons (title, subject_id) VALUES ('Practice', 20)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('Passed', 34, 42)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('Passed', 35, 42)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('Failed', 36, 42)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('Failed', 37, 42)

SELECT `value` FROM marks WHERE student_id = 42
SELECT title FROM books WHERE taken_by_student_id = 42

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