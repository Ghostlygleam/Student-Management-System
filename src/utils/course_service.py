def generate_transcripts(student_list, course_list):
    if not student_list:
        print("No students found.")
        return

    print("\nGenerating transcripts for students...")
    for student in student_list:
        print(f"\nTranscript for {student.email}:")
        if not student.enrolled_courses:
            print("  No enrolled courses.")
        else:
            for course_id in student.enrolled_courses:
                course = next((c for c in course_list if c.course_id == course_id), None)
                grades = student.grades.get(course_id, [])
                grades_str = ", ".join(grades) if grades else "No grades"
                print(f"  Course: {course.name if course else 'Unknown'} (ID: {course_id}), Grades: {grades_str}")
            print(f"  GPA: {student.calculate_gpa():.2f}")


def generate_course_statistics(course_list):
    if not course_list:
        print("No courses available.")
        return

    print("\nCourse Enrollment Statistics:")
    for course in course_list:
        enrolled_count = len(course.enrolled_students)
        capacity = course.capacity
        print(f"Course: {course.name} (ID: {course.course_id})")
        print(f"  Enrolled: {enrolled_count}/{capacity}")
        print(f"  Remaining spots: {capacity - enrolled_count}")
