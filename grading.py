#task1 (Grigorijs)
import json



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
#task3(Dev)
f= open("grading_data.json","r")
grade_data=json.load(f)
f.close()
def add_grade()
stuid=int(input("enter student id:"))
marks=int(input("enter new grade:"))
for student in grade_data["students":]
if student ["id"]==stuid:
    student["grades"]= student["grades"]+marks
    f= open("grading_data.json","w")
    json.dump(grade_data,f,indent=4)
    f.close()
    printf("grade added successfully")
    else return:
        printf("error,student not found")

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
    

    
