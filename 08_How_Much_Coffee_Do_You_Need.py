coffee_needed = 0
while True:
    commands = input()
    if commands == "END":
        break
    if commands == "coding" or commands == "dog" or commands == "cat" or commands == "movie":
        coffee_needed += 1
    elif commands == "CODING" or commands == "DOG" or commands == "CAT" or commands == "MOVIE":
        coffee_needed += 2
    else:
        continue

if coffee_needed > 5:
    print(f"You need extra sleep")
else:
    print(coffee_needed)