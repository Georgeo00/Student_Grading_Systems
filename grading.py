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
from fpdf import FPDF

from test import download_subject_report


#task1 (Grigorijs)
if os.path.exists("login_data.json"):
    with open("login_data.json", "r", encoding="utf-8") as f:
        login_data = json.load(f)

if os.path.exists("grading_data.json"):
    with open("grading_data.json", "r") as file:
        student_data = json.load(file)
if os.path.exists("classes.json"):           
    with open("classes.json", "r") as f:
        classes = json.load(f)


def download_all_students_report(data, output_file="all_students_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "All Students Grading Report", ln=True, align="C")
    pdf.ln(10)
    
    for cls in data:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Class: {cls['class']}", ln=True)
        pdf.ln(5)
        
        # Prepare header row
        headers = ["Student Name"] + [g['date'] for g in cls["students"][0]["grades"]]
        col_widths = [40] + [30] * len(headers[1:])
        
        # Table header
        pdf.set_font("Arial", "B", 12)
        for i, h in enumerate(headers):
            pdf.cell(col_widths[i], 10, h, border=1, align="C")
        pdf.ln()
        
        # Table rows
        pdf.set_font("Arial", size=12)
        for student in cls["students"]:
            row = [student["name"]] + [g["status"] for g in student["grades"]]
            for i, value in enumerate(row):
                pdf.cell(col_widths[i], 10, value, border=1, align="C")
            pdf.ln()
        
        pdf.ln(10)  # Space between classes
    
    pdf.output(output_file)
    print(f"PDF saved as {output_file}")


def download_single_student_report(data, student_name, output_file=None):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"{student_name} Report Card", ln=True, align="C")
    pdf.ln(10)
    
    for cls in data:
        student = next((s for s in cls["students"] if s["name"] == student_name), None)
        if not student:
            continue
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Class: {cls['class']}", ln=True)
        pdf.ln(5)
        
        # Table header
        pdf.set_font("Arial", "B", 12)
        headers = ["Date", "Grade"]
        col_widths = [50, 30]
        for i, h in enumerate(headers):
            pdf.cell(col_widths[i], 10, h, border=1, align="C")
        pdf.ln()
        
        # Table rows
        pdf.set_font("Arial", size=12)
        for g in student["grades"]:
            pdf.cell(col_widths[0], 10, g["date"], border=1, align="C")
            pdf.cell(col_widths[1], 10, g["status"], border=1, align="C")
            pdf.ln()
        
        pdf.ln(10)
    
    if output_file is None:
        output_file = f"{student_name}_report_card.pdf"
    
    pdf.output(output_file)
    print(f"PDF saved as {output_file}") 



def user_role(username, password, users):
    for admin in users["admins"]:
        if admin["username"] == username and admin["password"] == password:
            return "admin"

    for student in users["students"]:
        if student["username"] == username and student["password"] == password:
            return "student"
    for teacher in users["teachers"]:
        if teacher["username"] == username and teacher["password"] == password:
            
            return "teacher", teacher["role"]

# Task 3 - dev

def save_classes():

    f=open("classes.json","w")
    json.dump(classes,f,indent=4)
    f.close()


def add_grade_teacher(subject):

    student_name=input("Enter student name: ")
    date=input("Enter date: ")
    grade=input("Enter grade (or n): ")

    for cls in classes:
        if cls["class"].lower()==subject.lower():
            for student in cls["students"]:
                if student["name"]==student_name:
                    # Check if date already exists
                    for g in student["grades"]:
                        if g["date"]==date:
                            g["status"]=grade
                            save_classes()
                            print("Grade Updated")
                            return
                    student["grades"].append({ # --->If date not found, add new
                        "date": date,
                        "status": grade
                    })
                    save_classes()
                    print("Grade Added Successfully")
                    return

    print("Error: Student or Subject not found")


# task 4 (Neetee)adding students to Database using input
import json

def save_students(student_data):
    with open("classes.json", "w", encoding="utf-8") as f:
        json.dump(student_data, f, indent=4) 

def load_students():
    try:
        with open("classes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_logins(login_data):
    with open("login_data.json", "w", encoding="utf-8") as f:
        json.dump(login_data, f, indent=4)

def load_logins():
    try:
        with open("login_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# task 2(Daksh) 
class StudentManager:

    def __init__(self):
        self.data = {}

    def student_exists_by_name(self, name):
        for sid, student in self.data.items():
            if student["name"].lower() == name.lower():
                return sid
        return None
# Neetee's task continued
    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        # prevent duplicate names
        if self.student_exists_by_name(name):
            print("Student already exists.")
            return

        grades = []
        while True:
            grade = input("Enter grade (or 'done' to finish): ")
            if grade.lower() == "done":
                break
            grades.append(float(grade))

        student_id = str(len(self.data) + 1)

        self.data[student_id] = {
            "name": name,
            "age": age,
            "grades": grades
        }

        save_students(self.data)
        print("Student added successfully.")

    def add_grade_by_name(self):
        name = input("Enter student name: ")
        sid = self.student_exists_by_name(name)

        if not sid:
            print("Student not found.")
            return

        grade = float(input("Enter new grade: "))
        self.data[sid]["grades"].append(grade)

        save_students(self.data)
        print("Grade added successfully.")

    def show_students(self):
        for sid, student in self.data.items():
            print(f"\nID: {sid}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {student['grades']}")

    
    


# task 5 (Harshpreet) -> Checking grades. Outputting grades of a student from DB, will be used only by students, for admin and teacher will directly download pdf
    






#THIS PART LAST!!!
username_input = input("Enter username:")
password_input = input("Enter password:")
user, role = user_role(username_input, password_input, login_data)





# continuing task 5 (Harshpreet) -> Checking grades. Outputting grades of a student from DB, will be used only by students, for admin and teacher will directly download pdf
def check_student_grades(username_input, classes):
    print(f"{username_input} Student login successful") 

    while True:
        action = input("Choose action (check_grades, exit): ")

        if action == "check_grades":
            found = False

            # loop through classes 
            for cls in classes: 
                 # loop through students in the class to find the student with the matching username       
                    for student in cls["students"]:
                        if student.get("username") == username_input:
                            print(f"\nClass: {cls['class']}")
                            print(f"Grades for {student['name']}:")

                            # loop through the grades 

                            for i ,g in enumerate(student["grades"], start=1):
                                print(f"Subject{i} ({g['date']}): {g['status']}")

                                download_single_student_report(classes, student["name"])
                                print(f"Report card for {student['name']} downloaded successfully.")

                                found = True
                                break

                            if found:
                                break
                             
                        if not found:
                            print("No grades found for the student.")  
                            
                        elif action == "exit":
                         break

                        else :
                            print("Invalid action. Please try again.")
        elif user == "admin":

            print("Admin login successful")
            while True:
                action = input("Choose action (download_all_students_report, exit): ")

                if action == "download_all_students_report":
                    download_all_students_report(classes)
                    print("All students report downloaded successfully.")

                elif action == "exit":
                    break
                else:
                    print("Invalid action. Please try again.")

        elif user == "teacher":
            print(f"{role} Teacher login successful")
            while True:

                print("\n1. Add Grade")
                print("2. Download Subject Report")
                print("3. Exit")

                action = input("Choose: ")

                if action == "1":
                    add_grade_teacher(role)
                    print("Grade added successfully.")

                elif action == "2":
                    subject_name = input("Enter subject name: ")
                    download_subject_report(classes, subject_name)

                elif action == "3":
                    break
                else:
                    print("Invalid action. Please try again.")
        else:
            print("ACCESS DENIED.Invalid username or password.")

# 1️⃣ Download all students report
#download_all_students_report(classes)

#2️⃣ Download report card for a single student
#download_single_student_report(classes, "Student01")

# Download report for a specific subject
#download_subject_report(classes, role)
