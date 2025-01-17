from src.utils.course_service import add_course
from src.modules.student import Student
from src.utils.profile_service import view_student_profile
from src.utils.course_service import add_course, edit_course, delete_course

# List to store all courses
course_list = []

# Adding courses
add_course(course_list, course_id=101, name="Math 101", capacity=30)
add_course(course_list, course_id=102, name="Science 102", capacity=25)

# Editing a course
edit_course(course_list, course_id=101, new_name="Advanced Math", new_capacity=40)

# Deleting a course
delete_course(course_list, course_id=102)

# Display all remaining courses
print("\nAvailable Courses:")
for course in course_list:
    print(course)

# Create a sample student
student = Student(student_id=1, name="Alice", email="alice@example.com")

# Add some courses
student.add_course("Math 101")
student.add_course("Science 102")

# View the student's profile
view_student_profile(student)

