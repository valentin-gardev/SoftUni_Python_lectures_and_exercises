

class_a = {}
number_of_rows = int(input())

for _ in range(number_of_rows):
    student = input()
    grade = float(input())
    if student not in class_a:
        class_a[student] = []
        class_a[student].append(grade)
    else:
        class_a[student].append(grade)


for student, grades in class_a.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f'{student} -> {average_grade:.2f}')
    else:
        continue