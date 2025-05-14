while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue
    for i in string:
        print(i * 2, end="")
    print()
