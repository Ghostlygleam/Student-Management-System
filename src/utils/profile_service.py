def view_student_profile(student):
    print(f"Student ID: {student.student_id}")
    print(f"Name: {student.name}")
    print(f"Email: {student.email}")
    print("Enrolled Courses:")
    for course in student.enrolled_courses:
        print(f" - {course}")
