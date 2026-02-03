import json


#task1 (Grigorijs)
with open("login_data.json", "r", encoding="utf-8") as f:
    login_data = json.load(f)



def login_true(username, password, users):
    for user in users:
        if user["login"] == username and user["password"] == password:
            return True
    return False

username_input = input("Enter username:")
password_input = input("Enter password:")

if login_true(username_input, password_input, login_data):
    print("login successful")
else:
    print("Access denied")

# while login_true:
#task 2 (Daksh)

import json
import os
def load_students():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            return json.load(file)
    else:
        return {}
class StudentManager:

    def __init__(self, data):
        self.data = data

    def student_exists(self, sid):
        if sid in self.data:
            print("❌ Student already exists in database.")
            return True
        else:
            print("✅ Student not found. You can add this student.")
            return False
students = load_students()

manager = StudentManager(students)

student_id = input("Enter Student ID: ")

manager.student_exists(student_id)

#task3(Dev)
f= open("grading_data.json","r")
grade_data=json.load(f)
f.close()
def add_grade():
    stuid=int(input("enter student id:"))
    marks=int(input("enter new grade:"))
    for student in grade_data["students"]:
        if student ["id"]==stuid:
            student["grades"]= student["grades"]+marks
            f= open("grading_data.json","w")
            json.dump(grade_data,f,indent=4)
            f.close()
            printf("grade added successfully")
        else:
            printf("error,student not found")
            #if login=true
                  #printf(login succ)
                 # add grade

# task 4 (Neete)adding students to Database using input
students = []
next_id = 1

def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    student["id"] = next_id
    students.append(student)
    next_id += 1
    print("Student added successfully!")
# task 5 (Harshpreet) -> Checking grades. Outputting grades of a student from DB
    

    
