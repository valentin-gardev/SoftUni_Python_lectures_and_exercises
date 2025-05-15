num_wagons = int(input())
train = [0 for wagon in range(num_wagons)]

while True:
    commands = input().split()

    if 'End' in commands:
        break
    elif 'add' in commands:
        number_of_people = int(commands[1])
        train[-1] += number_of_people

    elif 'insert' in commands:
        index = int(commands[1])
        number_of_people = int(commands[2])
        train[index] += number_of_people


    elif 'leave' in commands:
        index = int(commands[1])
        number_of_people = int(commands[2])
        train[index] -= number_of_people



print(train)