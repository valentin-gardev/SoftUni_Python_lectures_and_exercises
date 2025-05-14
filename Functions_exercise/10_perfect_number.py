def finding_perfect_number(number):
    added_number = 0
    for x in range(1, number):
        if number % x == 0:
            added_number += x
    if added_number == number:
        return 'We have a perfect number!'
    return "It's not so perfect."


number_input = int(input())

print(finding_perfect_number(number_input))