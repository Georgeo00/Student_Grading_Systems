import json
from fpdf import FPDF

# Load your JSON data
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


def download_subject_report(data, subject_name, output_file=None):

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"{subject_name} Report", ln=True, align="C")
    pdf.ln(10)
    
    # Find the class
    cls = next((c for c in data if c["class"].lower() == subject_name.lower()), None)
    if not cls:
        print(f"No class found with name '{subject_name}'")
        return
    
    # Table header
    pdf.set_font("Arial", "B", 12)
    headers = ["Student Name"] + [g['date'] for g in cls["students"][0]["grades"]]
    col_widths = [50] + [30] * (len(headers) - 1)
    
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
    
    if output_file is None:
        output_file = f"{subject_name}_report.pdf"
    
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


# Example usage:

# 1️⃣ Download all students report
#download_all_students_report(classes)

#2️⃣ Download report card for a single student
#download_single_student_report(classes, "Student01")

#download report for a specific subject
#download_subject_report(classes, role)
