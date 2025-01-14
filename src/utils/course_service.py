from src.modules.course import Course
from src.modules.instructor import Instructor

def add_course(course_list, course_id, name, capacity):
    """
    Add a new course to the course list.
    :param course_list: List of existing courses
    :param course_id: Unique ID of the course
    :param name: Name of the course
    :param capacity: Maximum capacity of the course
    """
    for course in course_list:
        if course.course_id == course_id:
            print(f"Course with ID {course_id} already exists.")
            return

    new_course = Course(course_id, name, capacity)
    course_list.append(new_course)
    print(f"Course '{name}' has been added successfully!")
    
def edit_course(course_list, course_id, new_name=None, new_capacity=None):
    """
    Edit an existing course.
    :param course_list: List of existing courses
    :param course_id: ID of the course to edit
    :param new_name: New name for the course (optional)
    :param new_capacity: New capacity for the course (optional)
    """
    for course in course_list:
        if course.course_id == course_id:
            if new_name:
                course.name = new_name
            if new_capacity:
                course.capacity = new_capacity
            print(f"Course with ID {course_id} has been updated successfully!")
            return
    print(f"Course with ID {course_id} not found.")

def delete_course(course_list, course_id):
    """
    Delete an existing course from the course list.
    :param course_list: List of existing courses
    :param course_id: ID of the course to delete
    """
    for course in course_list:
        if course.course_id == course_id:
            course_list.remove(course)
            print(f"Course with ID {course_id} has been deleted successfully!")
            return
    print(f"Course with ID {course_id} not found.")
    
def assign_instructor_to_course(course, instructor):
    """
    Assign an instructor to a course.
    :param course: Instance of the Course class
    :param instructor: Instance of the Instructor class
    """
    if hasattr(course, 'instructor') and course.instructor:
        print(f"Course '{course.name}' already has an instructor assigned: {course.instructor.name}.")
        return

    course.instructor = instructor
    print(f"Instructor '{instructor.name}' has been assigned to course '{course.name}'.")
    
def enroll_student(course, student_id):
    """
    Enroll a student in a course if the course is not full.
    :param course: Instance of the Course class
    :param student_id: ID of the student to enroll
    """
    if course.is_full():
        print(f"Course '{course.name}' is full. Cannot enroll student ID {student_id}.")
    else:
        course.enrolled_students.append(student_id)
        print(f"Student ID {student_id} has been enrolled in course '{course.name}'.")
        
        
def enroll_student_in_course(course, student):
    """
    Enroll a student in a course if the course is not full.
    :param course: Instance of the Course class
    :param student: Instance of the Student class
    """
    if course.is_full():
        print(f"Course '{course.name}' is full. Cannot enroll student '{student.name}'.")
        return False
    else:
        course.enrolled_students.append(student.student_id)
        student.enroll_in_course(course)
        print(f"Student '{student.name}' has been enrolled in course '{course.name}'.")
        return True
    
def unenroll_student_in_course(course, student):
    """
    Unenroll a student from a course.
    :param course: Instance of the Course class
    :param student: Instance of the Student class
    """
    if student.student_id in course.enrolled_students:
        course.enrolled_students.remove(student.student_id)  # Удалить ID студента из списка курса
        student.enrolled_courses.remove(course.name)  # Удалить курс из списка студента
        print(f"Student '{student.name}' has been unenrolled from course '{course.name}'.")
        return True
    else:
        print(f"Student '{student.name}' is not enrolled in course '{course.name}'.")
        return False
def view_enrolled_students(course, student_list):
    """
    View all students enrolled in a specific course.
    :param course: Instance of the Course class
    :param student_list: List of all student instances
    """
    if not course.enrolled_students:
        print(f"No students are enrolled in the course '{course.name}'.")
        return

    print(f"Students enrolled in the course '{course.name}':")
    for student_id in course.enrolled_students:
        # Найти студента по его ID в student_list
        student = next((s for s in student_list if s.student_id == student_id), None)
        if student:
            print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")