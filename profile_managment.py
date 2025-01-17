#Importing pandas library
import pandas as pd
import csv
#Opening csv file
s_profiles_list = pd.read_csv("s_profiles_list.csv")



#Specifying class of the profiles
class student:
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email

#Creating class StudentProfile
class StudentProfile:
    def __init__ (self):
        self.profile = []
    
    #Creating function to add student profile
    def add_student(self, name, student_id, email):
        if student_id in s_profiles_list:
            print("Profile with this ID already exists \n")
        elif email in s_profiles_list:
            print("This email address is already in use \n")
        elif name in s_profiles_list:
            print("Student profile with this name already exists \n")
        else:
            s_profiles_list.append(name)
            s_profiles_list.append(student_id)
            s_profiles_list.append(email)
            print("Profile succesfully added \n")

    #Adding function to delete profiles
    def delete_profile(self, name, student_id, email):
        if name_dl in s_profiles_list:
            s_profiles_list.remove(name_dl)

    #Adding function to edit profiles  
    def edit_profile(self, name, student_id, email):
        edit_pr = input("Enter name of the profile to edit: \n")
        if edit_pr in s_profiles_list:



profile = StudentProfile()

#Executing the programm, using while loop
while True:
    action = input("Student Profile Management: \n"
                   "=========================== \n"
                   "Add Profile \n"
                   "Edit Profile \n"
                   "Delete Profile \n"
                   "Exit \n"
                   "=========================== \n")
    
    if action == "Exit":
        break
    elif action == "Add profile":
        name = input("Enter the student's name: ")
        student_id = int(input("Enter student's ID: "))
        email = input("Enter student's email: \n")
        profile.add_student(name, student_id, email)

    elif action == "Edit profile":
        ''
    elif action == "Delete profile":
        name_dl = input("Enter student profile name to delete: \n")
        if name_dl in s_profiles_list:
            profile.delete_profile(name_dl, student_id, email)
            print(f"Student {name_dl} profile deleted \n")
        else:
            print("Student profile not found \n")
     