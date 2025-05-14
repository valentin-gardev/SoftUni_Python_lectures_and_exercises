def receiving_numbers():
    number1 = int(input())
    number2 = int(input())
    return number1, number2


def factorial_numbers(number_one: int, number_two: int):
    factorial_first_number = 1
    factorial_second_number = 1
    for factorial in range(1, number_one + 1):
        factorial_first_number *= factorial
    for factorial in range(1, number_two + 1):
        factorial_second_number *= factorial
    return factorial_first_number, factorial_second_number

def devision_of_two_numbers(number_one: int, number_two: int):
    return number_one // number_two


first_number, second_number = receiving_numbers()
factorial_of_first_number, factorial_of_second_number = factorial_numbers(first_number, second_number)
devision_result = devision_of_two_numbers(factorial_of_first_number, factorial_of_second_number)

print(f'{devision_result:.2f}')
