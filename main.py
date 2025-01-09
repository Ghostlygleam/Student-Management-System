from src.utils.course_utils import add_course

# List to store all courses
course_list = []

# Adding courses
add_course(course_list, course_id=101, name="Math 101", capacity=30)
add_course(course_list, course_id=102, name="Science 102", capacity=25)

# Display all courses
print("\nAvailable Courses:")
for course in course_list:
    print(course)