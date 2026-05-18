from grading import avgrage_score, count_risk_levels

def build_report(student_name, score, grade, advice, risk_level):
    report= f"""\nStudent Performance Report
--------------------------
Student Name: {student_name}
Score: {score}
Grade: {grade}
Passed: {"True" if 50 <= score <= 100 else "False"}
Risk Level: {risk_level}
Advice: {advice}
"""
    return report


def risk_report(students):
    high_count, medium_count, low_count = count_risk_levels(students)

    report= f"""\nRisk Report 
--------------------------
High Count: {high_count}
Medium Count: {medium_count}
Low Count: {low_count}
"""
    return report

def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ','_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    return filename
