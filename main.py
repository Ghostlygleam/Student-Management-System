from src.utils.course_utils import add_course
from src.modules.student import Student
from src.utils.profile_service import view_student_profile

# List to store all courses
course_list = []

# Adding courses
add_course(course_list, course_id=101, name="Math 101", capacity=30)
add_course(course_list, course_id=102, name="Science 102", capacity=25)

# Display all courses
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

