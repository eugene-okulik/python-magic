INSERT INTO students (name, second_name, group_id) VALUES ('Peter', 'Parker', 2)
INSERT INTO books (title, taken_by_student_id) VALUES ('Biology', 11)
INSERT INTO books (title, taken_by_student_id) VALUES ('Chemistry', 11)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('DZ-01', 'Oct - 2023', 'Aug - 2023')
UPDATE students SET group_id = 19 where id = 23
INSERT INTO subjets (title) VALUES ('Chemistry')
INSERT INTO subjets (title) VALUES ('Biology')
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_one', 5)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_two', 5)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_one', 6)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_two', 6)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 5, 23)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 5, 23)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('C', 6, 23)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('D', 6, 23)

SELECT `value` FROM marks WHERE student_id = 23
SELECT title FROM books WHERE taken_by_student_id = 11

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

-- UPDATE books SET taken_by_student_id = 11 WHERE title  = 'Chemistry'
-- DELETE FROM students WHERE id = 22