from src.utils.course_service import add_course, edit_course, delete_course, assign_instructor_to_course, add_course, enroll_student
from src.modules.student import Student
from src.utils.profile_service import view_student_profile
from src.modules.course import Course
from src.modules.instructor import Instructor


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

# Create sample instructors
instructor_john = Instructor(instructor_id=1, name="John Doe")
instructor_jane = Instructor(instructor_id=2, name="Jane Smith")

# Assign instructors to courses if courses exist
if len(course_list) > 0:
    assign_instructor_to_course(course_list[0], instructor_john)  # Assign John to the first course

if len(course_list) > 1:
    assign_instructor_to_course(course_list[1], instructor_jane)  # Assign Jane to the second course
else:
    print("No second course available to assign an instructor.")
    
# Enroll students
enroll_student(course_list[0], student_id=1)  # Should succeed
enroll_student(course_list[0], student_id=2)  # Should succeed
enroll_student(course_list[0], student_id=3)  # Should fail (course is full)

# Display course details
print("\nCourse Details:")
for course in course_list:
    print(course)
    print(f"Enrolled Students: {course.enrolled_students}")
