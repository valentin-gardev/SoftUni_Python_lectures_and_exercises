
def grades_fun(grade_value: float):
    if 2 <= grade_value <= 2.99:
        return "Fail"
    elif 3 <= grade_value <= 3.49:
        return "Poor"
    elif 3.50 <= grade_value < 4.49:
        return "Good"
    elif 4.50 <= grade_value <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_value <= 6.00:
        return 'Excellent'



grades = float(input())

print(grades_fun(grades))