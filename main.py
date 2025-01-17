from src.utils.course_service import (
    add_course,
    enroll_student,
    unenroll_student,
    view_students,
    assign_grade, 
    display_gpa,
    display_transcript,
    generate_course_list,
)
from src.modules.course import Course
from src.modules.student import Student

course_list = []

add_course(course_list, course_id=101, name="Math 101", capacity=3)

student_1 = Student(student_id=1, name="Alice", email="alice@example.com")
student_2 = Student(student_id=2, name="Bob", email="bob@example.com")
student_3 = Student(student_id=3, name="Charlie", email="charlie@example.com")

print("\nEnrolling students:")
enroll_student(course_list[0], student_1)
enroll_student(course_list[0], student_2)
enroll_student(course_list[0], student_3)

print(f"DEBUG: Enrolled students in course '{course_list[0].name}': {course_list[0].enrolled_students}")

for student in [student_1, student_2, student_3]:
    print(f"DEBUG: Student {student.name} enrolled courses: {student.enrolled_courses}")

print("\nUpdated Student Details:")
for student in [student_1, student_2, student_3]:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

print("\nCourse Details:")
for course in course_list:
    print(course)

print("\nStudent Details:")
students = [student_1, student_2, student_3]
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

print("\nUnenrolling Students:")
unenroll_student(course_list[0], student_2)
unenroll_student(course_list[0], student_3)

print("\nUpdated Course Details:")
for course in course_list:
    print(course)
    print(f"Enrolled Students: {course.enrolled_students}")

print("\nUpdated Student Details:")
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Enrolled Courses: {student.enrolled_courses}")

enroll_student(course_list[0], student_2)
enroll_student(course_list[0], student_3)

print("\nViewing Enrolled Students:")
view_students(course_list[0], students)

print("\nAssigning Grades:")
assign_grade(student_1, 101, "A")
assign_grade(student_2, 101, "B")
assign_grade(student_3, 101, "C")

print("\nViewing Grades:")
for student in students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, Grades: {student.grades}")

assign_grade(student_1, 101, "B")
assign_grade(student_2, 101, "C")
assign_grade(student_3, 101, "A")

print("\nCalculating GPA:")
display_gpa(student_1)
display_gpa(student_2)
display_gpa(student_3)

print("\nGenerating Transcripts:")
display_transcript(student_1)
display_transcript(student_2)

generate_course_list(course_list)








