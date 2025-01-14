def view_student_profile(student):
    #Display the student's profile information
    print(f"Student ID: {student.student_id}")
    print(f"Name: {student.name}")
    print(f"Email: {student.email}")
    print("Enrolled Courses:")
    if student.enrolled_courses:
        for course in student.enrolled_courses:
            print(f" - {course}")
    else:
        print("No courses enrolled.")