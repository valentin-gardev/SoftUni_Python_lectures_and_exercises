number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number > 1000000:
        print("large positive")
    elif number < 1 and number != 0:
        print("small positive")
    else:
        print("positive")
elif number < 0:
    if number < -1000000:
        print("large negative")
    elif number > -1 and number != 0:
        print("small negative")
    else:
        print("negative")

