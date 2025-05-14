def password_checker(password: str):
    lenght_password = True
    only_letters_and_digits = True
    if not 6 <= len(password) and len(password) <= 10:
        lenght_password = False
    digits_in_password = 0
    for input in password:
        if input.isdigit():
            digits_in_password += 1
        if not input.isalpha() and not input.isdigit():
            only_letters_and_digits = False
            break
    return lenght_password, only_letters_and_digits, digits_in_password


password_input = input()
password_length, digits_letters, two_digits = password_checker(password_input)

if not password_length:
    print("Password must be between 6 and 10 characters")
if not digits_letters:
    print("Password must consist only of letters and digits")
if two_digits < 2:
    print("Password must have at least 2 digits")
if password_length and digits_letters and two_digits >= 2:
    print('Password is valid')