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




#task 2 (Daksh)

class StudentManager:

    def __init__(self, data):
        self.data = data

    def student_exists(self, sid):
        if sid in self.data:
            print("Student already exists in database.")
            return True
        else:
            print("Student not found. You can add this student.")
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
    


# task 5 (Harshpreet) -> Checking grades. Outputting grades of a student from DB, will be used only by students, for admin and teacher will directly download pdf
    






#THIS PART LAST!!!
username_input = input("Enter username:")
password_input = input("Enter password:")
user, role = user_role(username_input, password_input, login_data)






while user == "admin":
    print("admin login successful")

    action = input("choose action(add_students, check_grades): ")
    if action == "add_students":
        add_student()
    elif action == "add_grades":
        add_grade()
    elif action == "check_grades":
#        check_grades()   still to do
        print("in progress...")



while user == "user":
    print("user login successful")

    action = input("choose action(check_grades): ")


while user == "teacher":
    print (role," teacher login successful")





    
print("Access denied")


# 1️⃣ Download all students report
#download_all_students_report(classes)

#2️⃣ Download report card for a single student
#download_single_student_report(classes, "Student01")

# Download report for a specific subject
#download_subject_report(classes, role)
