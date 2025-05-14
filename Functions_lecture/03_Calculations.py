def calculator(operator, num1, num2):
    if operator == "subtract":
        return num1 - num2
    elif operator == 'divide':
        return num1 // num2
    elif operator == 'add':
        return num1 + num2
    elif operator == 'multiply':
        return num1 * num2







def calculator_input():
    operator = input()
    num1 = int(input())
    num2 = int(input())
    return calculator(operator, num1, num2)


print(calculator_input())