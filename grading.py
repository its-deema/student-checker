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