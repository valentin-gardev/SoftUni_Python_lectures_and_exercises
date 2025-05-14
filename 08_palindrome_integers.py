def palindrome_numbers(number):
    if number == number[::-1]:
        return True
    else:
        return False


numbers_to_check = input().split(', ')
result_for_palindrome = list(map(palindrome_numbers, numbers_to_check))
for result in result_for_palindrome:
    print(result)