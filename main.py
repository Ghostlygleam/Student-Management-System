from src.modules.student import Student
from src.utils.profile_service import view_student_profile

# Create a sample student
student = Student(student_id=1, name="Alice", email="alice@example.com")

# Add some courses
student.add_course("Math 101")
student.add_course("Science 102")

# View the student's profile
view_student_profile(student)