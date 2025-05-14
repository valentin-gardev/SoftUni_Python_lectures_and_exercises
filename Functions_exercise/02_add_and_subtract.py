def add_and_subtract(num1, num2, num3):
    def sum_numbers(num1, num2):
        return num1 + num2
    def subtract(num1, num2, num3):
        num4 = sum_numbers(num1, num2)
        return num4 - num3

    return subtract(num1, num2, num3)


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))