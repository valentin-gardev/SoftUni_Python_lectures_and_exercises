while True:
    name = input()
    house = ""
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        house += "Gryffindor."
    elif len(name) == 5:
        house += "Slytherin."
    elif len(name) == 6:
        house += "Ravenclaw."
    elif len(name) > 6:
        house += "Hufflepuff."
    print(f"{name} goes to {house}")