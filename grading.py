#to do:
#(DONE)add role based login(student/admin) 
#(DONE)refracture grading_data file so that it contains subjects
#add option to download the grades as pdf (y/n)
#delete the pdf after 24 hours 
#send an enquiry for missing subject test
#create checking grades function (task5))(Important)
#change functions like add_grades/check grades and add student so that they change data in classes.json
import json
import os


#task1 (Grigorijs)
if os.path.exists("login_data.json"):
    with open("login_data.json", "r", encoding="utf-8") as f:
        login_data = json.load(f)

if os.path.exists("grading_data.json"):
    with open("grading_data.json", "r") as file:
        student_data = json.load(file)    



def user_role(username, password, users):
    for admin in users["admins"]:
        if admin["username"] == username and admin["password"] == password:
            return "admin"

    for student in users["students"]:
        if student["username"] == username and student["password"] == password:
            return "student"




#task 2 (Daksh)

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

#student_id = input("Enter Student ID: ")#could change so that it check for the name instead, because admin(teacher) will probably not know the id of a student (Greg)
#manager = StudentManager(student_data)

#manager.student_exists(student_id)

#task3(Dev)
def add_grade():
    stuid=int(input("enter student id:"))
    marks=int(input("enter new grade:"))
    for student in student_data["students"]:
        if student ["id"]==stuid:
            student["grades"]= student["grades"]+marks
            f= open("grading_data.json","w")
            json.dump(student_data,f,indent=4)
            f.close()
            print("grade added successfully")#use print instead of printf in python
        else:
            print("error,student not found")
            #if login=true
                  #printf(login succ)
                 # add grade

# task 4 (Neetee)adding students to Database using input
def save_students(student_data):
    with open("grading_py.json", "w", encoding="utf-8") as f:
        json.dump(student_data, f, indent=4)

def add_student():                              #add checking if student already exists (from daksh code)
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")     #not sure if how will it work with multiple grades
    next_id = len(student_data) + 1
    student = {
        "name": name,
        "age": age,
        "grade": grade    }
    student_data.append(student)
    next_id += 1
    save_students("grading_py.json", student_data) #why create save_students?
    print("Student added successfully!")
    


# task 5 (Harshpreet) -> Checking grades. Outputting grades of a student from DB
    

username_input = input("Enter username:")
password_input = input("Enter password:")





while user_role(username_input, password_input, login_data) == "admin":
    print("admin login successful")

    action = input("choose action(add_students, add_grades, check_grades): ")
    if action == "add_students":
        add_student()
    elif action == "add_grades":
        add_grade()
    elif action == "check_grades":
#        check_grades()   still to do
        print("in progress...")



while user_role(username_input, password_input, login_data) == "user":
    print("user login successful")

    action = input("choose action(check_grades): ")




    
print("Access denied")
