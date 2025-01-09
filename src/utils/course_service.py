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