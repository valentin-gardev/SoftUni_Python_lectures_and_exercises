registered_users = {}

course_input = input().split(' : ')

while course_input[0] != 'end':
    course_name, student_name = course_input
    if course_name not in registered_users:
        registered_users[course_name] = []
        registered_users[course_name].append(student_name)
    else:
        registered_users[course_name].append(student_name)
    course_input = input().split(' : ')

for course in registered_users:
    print(f'{course}: {len(registered_users[course])}')
    list_students = registered_users[course]
    for student in list_students:
        print(f'-- {student}')


