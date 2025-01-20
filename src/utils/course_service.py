from src.modules.course import Course
from src.modules.instructor import Instructor

def add_course(course_list, course_id, name, capacity):
    # Check if a course with the given ID already exists to avoid duplicates
    for course in course_list:
        if course.course_id == course_id:
            print(f"Course with ID {course_id} already exists.")
            return

    # Create a new course and add it to the list
    new_course = Course(course_id, name, capacity)
    course_list.append(new_course)
    print(f"Course '{name}' has been added successfully!")
    
def edit_course(course_list, course_id, new_name=None, new_capacity=None):
    # Edit an existing course by ID
    for course in course_list:
        if course.course_id == course_id:
            # Update the course name if a new one is provided
            if new_name:
                course.name = new_name
            # Update the course capacity if a new one is provided
            if new_capacity:
                course.capacity = new_capacity
            print(f"Course with ID {course_id} has been updated successfully!")
            return
    # Inform the user if the course was not found
    print(f"Course with ID {course_id} not found.")

def delete_course(course_list, course_id):
    # Remove a course from the list by ID
    for course in course_list:
        if course.course_id == course_id:
            if course.enrolled_students:
                raise Exception(f"Can't delete course with ID {course_id} because it has enrolled students")
            course_list.remove(course)
            print(f"Course with ID {course_id} has been deleted successfully!")
            return
    raise ValueError(f"Course with ID {course_id} does not exist.")
    
def assign_instructor_to_course(course, instructor):
    # Check if the course already has an assigned instructor
    if hasattr(course, 'instructor') and course.instructor:
        print(f"Course '{course.name}' already has an instructor assigned: {course.instructor.name}.")
        return

    # Assign a new instructor to the course
    course.instructor = instructor
    print(f"Instructor '{instructor.name}' has been assigned to course '{course.name}'.")
    
def enroll_student(course, student_id):
    # Check if the course has space for more students
    if course.is_full():
        print(f"Course '{course.name}' is full. Cannot enroll student ID {student_id}.")
    else:
        # Add the student to the course's enrolled list
        course.enrolled_students.append(student_id)
        print(f"Student ID {student_id} has been enrolled in course '{course.name}'.")
        
        
def enroll_student_in_course(course, student):
    # Check if the course has available capacity before enrolling the student
    if course.is_full():
        print(f"Course '{course.name}' is full. Cannot enroll student '{student.name}'.")
    else:
        # Add the student to the course's enrolled list and update the student's records
        course.enrolled_students.append(student.student_id) 
        student.enroll_in_course(course) 
        print(f"Student '{student.name}' has been enrolled in course '{course.name}'.")
    
def unenroll_student_in_course(course, student):
    # Remove the student from the course if they are currently enrolled
    if student.student_id in course.enrolled_students:
        course.enrolled_students.remove(student.student_id) 
        student.enrolled_courses.remove(course.course_id) 
        print(f"Student '{student.name}' has been unenrolled from course '{course.name}'.")
    else:
        # Inform if the student was not enrolled in the course
        print(f"Student '{student.name}' is not enrolled in course '{course.name}'.")
        
def view_enrolled_students(course, student_list):
    # Check if there are any students enrolled in the course
    if not course.enrolled_students:
        print(f"No students are enrolled in the course '{course.name}'.")
        return

    # Display a list of students enrolled in the course
    print(f"Students enrolled in the course '{course.name}':")
    for student_id in course.enrolled_students:
        student = next((s for s in student_list if s.student_id == student_id), None)
        if student:
            print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")
            
def assign_grade_to_student(student, course_id, grade):
    # Assign a grade to the student if they are enrolled in the course
    if course_id in student.enrolled_courses:
        student.assign_grade(course_id, grade)
        print(f"Grade '{grade}' has been assigned to student '{student.name}' for course ID '{course_id}'.")
    else:
        # Inform if the student is not enrolled in the course
        print(f"Student '{student.name}' is not enrolled in course ID '{course_id}'.")
        
def display_student_gpa(student):
    # Calculate and display the student's GPA
    gpa = student.calculate_gpa()
    print(f"Student '{student.name}' has a GPA of {gpa:.2f}.")
    
def display_transcript(student):
    # Display the academic transcript of the student
    print(student.generate_transcript())
    
def generate_course_list(course_list):
    # Generate and display a list of all courses with enrollment data
    print("\nCourse List with Enrollment Data:")
    for course in course_list:
        print(course.get_summary())

