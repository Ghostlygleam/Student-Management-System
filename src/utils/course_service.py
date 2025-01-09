from src.modules.course import Course

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