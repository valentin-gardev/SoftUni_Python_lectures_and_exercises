amount_of_numbers = int(input())
amount = 0
for _ in range(amount_of_numbers):
    number = int(input())
    if number % 2 == 1:
        print(f"{number} is odd!")
        break
    elif number % 2 != 1:
        amount += 1
        if amount == amount_of_numbers:
            print(f"All numbers are even.")