def is_valid_score(score):
    return score >= 0 and score <= 100


def classify_score(score):
    if score >= 85:
        return"Excelent"
    elif score >= 50:
        return "Passed"
    else :
        return "Faild"

def avgrage_score(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def get_risk_level(score):
    if score >= 70 :
        return "Low"
    elif score >=50:
        return "Medium"
    else:
        return "High"
    
def get_support_advice(score):
    if score < 50:
        return "The student needs support"
    elif score <= 69:
        return "The student should practice more"
    else:
        return "Keep improving and continue"
    
def count_risk_levels(students):
   high_count = 0
   medium_count = 0
   low_count = 0
   
   for student in students:
       if student["risk_level"] == "High":
           high_count += 1
       elif student["risk_level"] == "Medium":
           medium_count += 1
       else:
           low_count += 1
   return high_count, medium_count, low_count