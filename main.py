from src.utils.course_service import (
    add_course,
    enroll_student_in_course,
    unenroll_student_in_course,
)
from src.modules.course import Course
from src.modules.student import Student

# Create a list to store courses
course_list = []  # Объявление списка курсов

# Step 1: Adding courses
add_course(course_list, course_id=101, name="Math 101", capacity=2)

# Step 2: Creating students
student_1 = Student(student_id=1, name="Alice", email="alice@example.com")
student_2 = Student(student_id=2, name="Bob", email="bob@example.com")
student_3 = Student(student_id=3, name="Charlie", email="charlie@example.com")

# Step 3: Enroll students
print("\nEnrolling students:")
enroll_student_in_course(course_list[0], student_1)
enroll_student_in_course(course_list[0], student_2)
enroll_student_in_course(course_list[0], student_3)  # Should fail (course is full)

# Step 4: Display course details
print("\nCourse Details:")
for course in course_list:
    print(course)

# Step 5: Display student details
print("\nStudent Details:")
students = [student_1, student_2, student_3]
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

# Step 6: Unenroll students
print("\nUnenrolling Students:")
unenroll_student_in_course(course_list[0], student_2)  # Unenroll Bob
unenroll_student_in_course(course_list[0], student_3)  # Attempt to unenroll Charlie (not enrolled)

# Step 7: Display updated course details
print("\nUpdated Course Details:")
for course in course_list:
    print(course)
    print(f"Enrolled Students: {course.enrolled_students}")

# Step 8: Display updated student details
print("\nUpdated Student Details:")
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

