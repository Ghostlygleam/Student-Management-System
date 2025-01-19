import csv
import os
import hashlib
from src.modules.student import Student
from src.modules.instructor import Instructor
from src.modules.admin import Admin
from src.utils.auth_service import Authentication
from src.modules.course import Course

# Путь к файлу с пользователями
user_file = os.path.join(os.getcwd(), "users.csv")

# Списки пользователей
student_list = []
instructor_list = []
auth = Authentication(user_file)

# Глобальный список курсов
course_list = []
course_file = os.path.join(os.getcwd(), "courses.csv")


def load_courses():
    """
    Загружает курсы из courses.csv в память.
    """
    print(f"Loading courses from {course_file}...")
    try:
        with open(course_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                course = Course(
                    course_id=int(row["id"]),
                    name=row["name"].strip(),  # Убираем лишние пробелы
                    capacity=int(row["capacity"]),
                )
                course.instructor = row["instructor_email"].strip() if row["instructor_email"] else None
                course_list.append(course)
                print(f"Loaded course: {course}")  # Лог загруженного курса
        print("Courses successfully loaded.")
    except FileNotFoundError:
        print(f"File {course_file} not found. Starting with an empty course list.")
    except Exception as e:
        print(f"Error loading courses: {e}")
    print("Available courses in memory:")
    for course in course_list:
        print(course)






def save_courses():
    """
    Сохраняет все курсы в файл courses.csv.
    """
    print("Saving courses...")
    try:
        with open(course_file, "w", newline="") as file:
            fieldnames = ["id", "name", "capacity", "instructor_email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for course in course_list:
                writer.writerow({
                    "id": course.course_id,
                    "name": course.name,
                    "capacity": course.capacity,
                    "instructor_email": course.instructor or ""
                })
        print(f"Courses successfully saved to {course_file}.")
    except Exception as e:
        print(f"Error saving courses: {e}")


def load_users():
    """
    Загружает пользователей из CSV в память.
    """
    print(f"Loading users from {user_file}...")
    try:
        with open(user_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                role = row["role"].lower()
                email = row["email"]
                name = row.get("name", "Unnamed User")
                user_id = int(row.get("id", 0))
                if role == "student":
                    student = Student(student_id=user_id, name=name, email=email)
                    student_list.append(student)
                elif role == "instructor":
                    instructor = Instructor(instructor_id=user_id, name=name, email=email)
                    instructor_list.append(instructor)
                # Загружаем данные в систему аутентификации
                auth.users[email] = {"password": row["password"], "role": role}
        print("Users successfully loaded.")
    except FileNotFoundError:
        print(f"File {user_file} not found. Starting with an empty database.")
    except Exception as e:
        print(f"Error loading users: {e}")


def save_users():
    """
    Сохраняет всех пользователей в файл users.csv.
    """
    print("Saving users...")
    try:
        with open(user_file, "w", newline="") as file:
            fieldnames = ["id", "name", "email", "password", "role"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Сохранение студентов
            for student in student_list:
                writer.writerow({
                    "id": student.student_id,
                    "name": student.name,
                    "email": student.email,
                    "password": auth.users[student.email]["password"],
                    "role": "student"
                })

            # Сохранение инструкторов
            for instructor in instructor_list:
                writer.writerow({
                    "id": instructor.instructor_id,
                    "name": instructor.name,
                    "email": instructor.email,
                    "password": auth.users[instructor.email]["password"],
                    "role": "instructor"
                })

            # Сохранение администраторов
            for email, data in auth.users.items():
                if data["role"] == "admin":
                    writer.writerow({
                        "id": "0",  # Фиксированный ID для администратора
                        "name": "Admin Name",
                        "email": email,
                        "password": data["password"],
                        "role": "admin"
                    })

        print(f"Users successfully saved to {user_file}.")
    except Exception as e:
        print(f"Error saving users: {e}")
        



def register_user(email, password, role):
    """
    Регистрирует нового пользователя в системе.
    """
    global student_list, instructor_list
    if email in auth.users:
        print(f"User '{email}' already exists!")
        return

    if role == "student":
        student_id = len(student_list) + 1
        student = Student(student_id=student_id, name="Student Name", email=email)
        student_list.append(student)
    elif role == "instructor":
        instructor_id = len(instructor_list) + 1
        instructor = Instructor(instructor_id=instructor_id, name="Instructor Name", email=email)
        instructor_list.append(instructor)
    elif role == "admin":
        print(f"Registering admin with email {email}.")
        auth.users[email] = {"password": hashlib.sha256(password.encode()).hexdigest(), "role": "admin"}
    else:
        print("Invalid role specified. Please choose 'student', 'instructor', or 'admin'.")
        return

    auth.register_user(email, password, role)
    save_users()

def admin_menu():
    """
    Меню для администратора.
    """
    while True:
        print("\nAdmin Menu:")
        print("===========================")
        print("1. View All Users")
        print("2. Add New User")
        print("3. View All Courses")
        print("4. Add New Course")
        print("5. Assign Instructor to Course")
        print("6. Logout")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            print("\nRegistered Users:")
            for email, data in auth.users.items():
                print(f"Email: {email}, Role: {data['role']}")
        elif action == "2":
            email = input("Enter new user's email: ")
            password = input("Enter new user's password: ")
            role = input("Enter new user's role (admin/student/instructor): ").lower()
            register_user(email, password, role)
        elif action == "3":
            print("\nAll Courses:")
            for course in course_list:
                print(f"ID: {course.course_id}, Name: {course.name}, Capacity: {course.capacity}, Instructor: {course.instructor or 'None'}")
        elif action == "4":
            course_id = len(course_list) + 1
            name = input("Enter course name: ")
            capacity = int(input("Enter course capacity: "))
            course = Course(course_id=course_id, name=name, capacity=capacity)
            course_list.append(course)
            save_courses()
            print(f"Course '{name}' added successfully.")
        elif action == "5":
            try:
                course_id = int(input("Enter course ID: "))
                instructor_email = input("Enter instructor's email: ")
                course = next((c for c in course_list if c.course_id == course_id), None)
                instructor = next((i for i in instructor_list if i.email == instructor_email), None)

                if not course:
                    print(f"Course with ID {course_id} does not exist.")
                elif not instructor:
                    print(f"Instructor with email {instructor_email} does not exist.")
                else:
                    course.instructor = instructor_email
                    save_courses()
                    print(f"Instructor '{instructor_email}' assigned to course '{course.name}'.")
            except ValueError:
                print("Invalid input. Course ID must be a number.")

        elif action == "6":
            print("Logging out of Admin Panel...")
            break
        else:
            print("Invalid option. Please choose again.")


def student_menu(student_email):
    """
    Меню для студента.
    """
    # Ищем текущего студента в списке студентов по email
    current_student = next((s for s in student_list if s.email == student_email), None)
    if not current_student:
        print("Student profile not found.")
        return

    while True:
        print("\nStudent Menu:")
        print("===========================")
        print("1. View Enrolled Courses")
        print("2. Enroll in a Course")
        print("3. View Grades and GPA")
        print("4. Logout")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            # Просмотр записанных курсов
            print("\nEnrolled Courses:")
            if current_student.enrolled_courses:
                for course in current_student.enrolled_courses:
                    print(f"- {course}")
            else:
                print("You are not enrolled in any courses.")

        elif action == "2":
            try:
                course_name = input("Enter the name of the course to enroll in: ").strip().lower()
                course = next((c for c in course_list if c.name.lower() == course_name), None)

                if not course:
                    print(f"Course '{course_name}' does not exist.")
                elif len(course.enrolled_students) >= course.capacity:
                    print(f"Course '{course.name}' is full. Cannot enroll.")
                else:
                    current_student.enroll_in_course(course.name)
                    course.enrolled_students.append(current_student)
                    print(f"You have been enrolled in '{course.name}'.")
                    save_courses()
            except Exception as e:
                print(f"An error occurred: {e}")



        elif action == "3":
            # Просмотр оценок и расчёт GPA
            print("\nYour Grades:")
            for course_id, grade in current_student.grades.items():
                print(f"Course: {course_id}, Grade: {grade}")
            gpa = current_student.calculate_gpa()
            print(f"Your GPA: {gpa:.2f}")

        elif action == "4":
            print("Logging out of Student Dashboard...")
            break

        else:
            print("Invalid option. Please choose again.")


def instructor_menu(instructor_email):
    """
    Меню для преподавателя.
    """
    # Определяем текущего инструктора по email
    current_instructor = next((i for i in instructor_list if i.email == instructor_email), None)
    if not current_instructor:
        print("Instructor profile not found.")
        return

    while True:
        print("\nInstructor Menu:")
        print("===========================")
        print("1. View Assigned Courses")
        print("2. Assign Grade to Student")
        print("3. Logout")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            print("\nAssigned Courses:")
            assigned_courses = [course for course in course_list if course.instructor and course.instructor.lower() == instructor_email.lower()]
            if assigned_courses:
                for course in assigned_courses:
                    print(f"Course ID: {course.course_id}, Name: {course.name}, Capacity: {course.capacity}")
            else:
                print("No courses assigned yet.")
        elif action == "2":
            try:
                student_email = input("Enter the email of the student: ")
                course_id = int(input("Enter the course ID: "))
                grade = input("Enter the grade (A-F): ").upper()

                student = next((s for s in student_list if s.email == student_email), None)
                course = next((c for c in course_list if c.course_id == course_id), None)

                if not student:
                    print("Student not found.")
                elif not course:
                    print("Course not found.")
                elif course.instructor and course.instructor.lower() != instructor_email.lower():
                    print("You are not assigned to this course.")
                else:
                    # Используем текущего инструктора для назначения оценки
                    current_instructor.assign_grade(student, course_id, grade)
                    print(f"Grade '{grade}' assigned to student '{student.name}' for course '{course.name}'.")
            except ValueError:
                print("Invalid input. Course ID must be a number.")
        elif action == "3":
            print("Logging out of Instructor Dashboard...")
            break
        else:
            print("Invalid option. Please choose again.")






def authentication_menu():
    """
    Меню аутентификации.
    """
    while True:
        print("\nAuthentication Menu:")
        print("===========================")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role = input("Enter your role (admin/student/instructor): ").lower()

            if email and password:
                register_user(email, password, role)
            else:
                print("Email and password are required for registration.")

        elif action == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role = auth.login_user(email, password)

            if role == "admin":
                admin_menu()
            elif role == "student":
                student_menu(email)
            elif role == "instructor":
                instructor_menu(email)
            else:
                print("Invalid role or authentication failed.")

        elif action == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")



if __name__ == "__main__":
    load_users()
    load_courses()
    authentication_menu()
