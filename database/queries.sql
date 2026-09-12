-- Week 2: Complex SQL Queries
-- Student Course Management Database


-- 1. Count the total number of students
SELECT COUNT(*) AS total_students
FROM students;


-- 2. Find the average age of students
SELECT AVG(age) AS average_age
FROM students;


-- 3. Count the total number of enrollments
SELECT COUNT(*) AS total_enrollments
FROM enrollments;


-- 4. Count students enrolled in each course
SELECT
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY total_students DESC;


-- 5. Show the number of enrollments for each course
SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY enrollment_count DESC;


-- 6. Find the average student age in each course
SELECT
    c.course_name,
    AVG(s.age) AS average_student_age
FROM courses c
JOIN enrollments e
    ON c.course_id = e.course_id
JOIN students s
    ON e.student_id = s.student_id
GROUP BY c.course_name
ORDER BY average_student_age DESC;


-- 7. Show courses having more than one enrollment
SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING COUNT(e.enrollment_id) > 1
ORDER BY enrollment_count DESC;