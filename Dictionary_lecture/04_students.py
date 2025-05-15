students = {}
while True:
    student = input().split(':')
    if len(student) <= 1:
        course_check = ''.join(student).replace('_', ' ')
        for name, ID in students.items():
            for ID1, course in ID.items():
                if course == course_check:
                    print(f'{name} - {ID1}')

        break

    name, ID, course = student
    students[name] = {}
    students[name][ID] = course

