from grading import avgrage_score

def build_report(student_name, score, status, advice):
    report= f"""\nStudent Performance Report
--------------------------
Student Name: {student_name}
Score: {score}
Status: {status}
Passed: {"True" if 50 <= score <= 100 else "False"}
Advice: {advice}
"""
    return report

def advice_writer(score):
    if score >= 85:
        return "Keep it up the great work and start exploring advanced exercises"
    elif score >=70:
        return "Keep practicing and fix small mistakes"
    elif score >= 50:
        return "you passed, but more practice will help"
    else:
        return "Review the basics and seek extra support"

def score_report(score_array):
    report= f"""\nScore Report 
--------------------------
Average Score: {avgrage_score(score_array)}
Highest Score: {max(score_array)}
Lowest Score:" {min(score_array)}
"""
    return report

def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ','_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    return filename
