from grading import is_valid_score, classify_score,avgrage_score
from report_writer import save_report, build_report, score_report, advice_writer


score_array = []

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
                score_array.append(score)
                status = classify_score(score)
                advice = advice_writer(score)
                report = build_report(student_name, score, status,advice)
                filename = save_report(student_name, report)

                print(report)
                print(f"report saved to: {filename}")
    except ValueError:
        print("Invalid input, Score must be a number.")

print(score_report(score_array))


