n = int(input())
lst_numbers = []

for _ in range(n):
    numbers = int(input())
    lst_numbers.append(numbers)

command = input()

for num in lst_numbers[:]:
    if command == "even":
        if num % 2 != 0:
            lst_numbers.remove(num)

    elif command == "odd":
        if num % 2 == 0:
            lst_numbers.remove(num)

    elif command == "negative":
        if num >= 0:
            lst_numbers.remove(num)

    elif command == "positive":
        if num < 0:
            lst_numbers.remove(num)

print(lst_numbers)