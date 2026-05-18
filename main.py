from grading import is_valid_score, classify_score,get_risk_level , get_support_advice
from report_writer import save_report, build_report, risk_report


students = []
# loops until the user enter 'q'
while True:

    try:
        student_name = input("\nEnter student name (or 'q' to quit): ").strip()

        # exsit the loop and print the avg, max , min scores
        if student_name.lower() == 'q':
            print("Exiting...")
            break   

        if student_name == "" :
            print("student name can't be empty")

        else:
            score = float(input("Enter student score from 0 to 100 :"))
            if not is_valid_score(score):
                print("score must be between 0 and 100")
            
            else:
                grade = classify_score(score)
                advice = get_support_advice(score)
                risk_level = get_risk_level(score)
                report = build_report(student_name, score, grade, advice, risk_level)
                filename = save_report(student_name, report)
                student_dic = {
                    "name" : student_name,
                    "score" : score,
                    "grade" : grade,
                    "passed" : "True" if 50 <= score <= 100 else "False",
                    "risk_level" : risk_level,
                    "advice" : advice
                }
                students.append(student_dic)
                print(report)
                print(risk_report(students))

                print(f"report saved to: {filename}")
    except ValueError:
        print("Invalid input, Score must be a number.")



