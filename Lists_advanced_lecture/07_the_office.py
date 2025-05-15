from functools import reduce

happiness = list(map(int, input().split()))
factor = int(input())

employee_happiness = list(map(lambda x: x * factor, happiness))
average_happiness = reduce(lambda x, y: x + y, employee_happiness) / len(happiness)
above_average_employees = list(filter(lambda x: x > average_happiness, employee_happiness))
if len(above_average_employees) >= len(happiness) / 2:
    print(f'Score: {len(above_average_employees)}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {len(above_average_employees)}/{len(happiness)}. Employees are not happy!')
print()