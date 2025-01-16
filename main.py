from src.utils.course_service import (
    add_course,
    enroll_student_in_course,
    unenroll_student_in_course,
    view_enrolled_students,
    assign_grade_to_student,  # Added for Task 16
)
from src.modules.course import Course
from src.modules.student import Student

course_list = []  

# Adding courses
add_course(course_list, course_id=101, name="Math 101", capacity=3)

# Creating students
student_1 = Student(student_id=1, name="Alice", email="alice@example.com")
student_2 = Student(student_id=2, name="Bob", email="bob@example.com")
student_3 = Student(student_id=3, name="Charlie", email="charlie@example.com")

# Enroll students
print("\nEnrolling students:")
enroll_student_in_course(course_list[0], student_1)  # Зачисляем Alice
enroll_student_in_course(course_list[0], student_2)  # Зачисляем Bob
enroll_student_in_course(course_list[0], student_3)  # Зачисляем Charlie (если курс не полный)

print(f"DEBUG: Enrolled students in course '{course_list[0].name}': {course_list[0].enrolled_students}")

for student in [student_1, student_2, student_3]:
    print(f"DEBUG: Student {student.name} enrolled courses: {student.enrolled_courses}")


# Display updated student details
print("\nUpdated Student Details:")
for student in [student_1, student_2, student_3]:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

# Display course details
print("\nCourse Details:")
for course in course_list:
    print(course)

# Display student details
print("\nStudent Details:")
students = [student_1, student_2, student_3]
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

# Unenroll students
print("\nUnenrolling Students:")
unenroll_student_in_course(course_list[0], student_2)  
unenroll_student_in_course(course_list[0], student_3) 

# Display updated course details
print("\nUpdated Course Details:")
for course in course_list:
    print(course)
    print(f"Enrolled Students: {course.enrolled_students}")

# Display updated student details
print("\nUpdated Student Details:")
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")
    
# View all students enrolled in a course
print("\nViewing Enrolled Students:")
view_enrolled_students(course_list[0], students)

enroll_student_in_course(course_list[0], student_3)
enroll_student_in_course(course_list[0], student_2)


# Assign grades to students
print("\nAssigning Grades:")
assign_grade_to_student(student_1, 101, "A")  # Assign grade to Alice
assign_grade_to_student(student_2, 101, "B")  # Assign grade to Bob
assign_grade_to_student(student_3, 101, "C")  # Should fail (not enrolled)


# View student grades
print("\nViewing Grades:")
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Grades: {student.grades}")







