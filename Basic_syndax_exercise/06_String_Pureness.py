number_of_strings = int(input())

for _ in range(number_of_strings):
    string = input()
    is_it_pure = True
    for i in string:
        if i == "," or i == "." or i == "_":
            is_it_pure = False

    if is_it_pure == True:
        print(f"{string} is pure.")
    elif is_it_pure == False:
        print(f"{string} is not pure!")
