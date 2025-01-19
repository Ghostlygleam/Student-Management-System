#Importing pandas library
import pandas as pd
from src.modules.student import Student




#Creating class StudentProfile
class StudentProfile:
    def __init__(self):
        try:
            self.s_profiles_list = pd.read_csv("s_profiles_list.csv")
        except FileNotFoundError:
            self.s_profiles_list = pd.DataFrame(columns=['name', 'student_id', 'email'])
    
    #Creating function to add student profile
    def add_student(self, name, student_id, email):
        if student_id in self.s_profiles_list['student_id'].values:
            print("Profile with this ID already exists \n")
        elif email in self.s_profiles_list['email'].values:
            print("This email address is already in use \n")
        elif name in self.s_profiles_list['name'].values:
            print("Student profile with this name already exists \n")
        else:
            new_row = pd.DataFrame([{'name': name, 'student_id': student_id, 'email': email}])
            self.s_profiles_list = pd.concat([self.s_profiles_list, new_row], ignore_index=True)
            print("Profile successfully added \n")

    #Adding function to delete profiles
    def delete_profile(self, name_dl):
        if name_dl in self.s_profiles_list['name'].values:
            self.s_profiles_list = self.s_profiles_list[self.s_profiles_list['name'] != name_dl]
            print(f"Profile {name_dl} deleted \n")
        else:
            print("Profile not found\n")

    #Adding function to edit profiles  
    def edit_profile(self, old_name):
        for index, row in self.s_profiles_list.iterrows():
            if row['name'] == old_name:
                row['name'] = input("New name (leave empty to skip): ") or row['name']
                try:
                    row['student_id'] = int(input("New student ID (leave empty to skip): ") or row['student_id'])
                except ValueError:
                    print("Invalid ID. Keeping the current value.")
                row['email'] = input("New email (leave empty to skip): ") or row['email']
                print("Profile updated successfully \n")
                return
        print("Profile not found \n")



profile = StudentProfile()

#Executing the programm, using while loop
# while True:
#     action = input("Student Profile Management: \n"
#         "=========================== \n"
#         "Add Profile \n"
#         "Edit Profile \n"
#         "Delete Profile \n"
#         "Exit \n"
#         "=========================== \n").strip().lower()
    
#     if action == "Exit":
#         break
#     elif action == "Add profile":
#         name = input("Enter the student's name: ")
#         try:
#             student_id = int(input("Enter student's ID: "))
#         except ValueError:
#             print("Wrong id, please enter a number")
#             continue
#         email = input("Enter student's email: \n")
#         profile.add_student(name, student_id, email)

#     elif action == "Edit profile":
#         old_name = input("enter the name of the profile:")
#         new_name = input("Enter the new name of the profile")
#         try:
#             student_id = int(input("Enter the new ID "))
#         except ValueError:
#             print("Wrong id")
#             continue
#     elif action == "Delete profile":
#         name_dl = input("Enter student profile name to delete: \n")
#         if name_dl in s_profiles_list:
#             profile.delete_profile(name_dl, student_id, email)
#             print(f"Student {name_dl} profile deleted \n")
#         else:
#             print("Student profile not found \n")