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

