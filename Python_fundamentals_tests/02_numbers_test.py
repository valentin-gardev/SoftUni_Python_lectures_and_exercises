numbers = input().split()
numbers = [int(i) for i in numbers]
def commands(command):
    global numbers
    if 'Add' in command:
        command.pop(0)
        for i in command:
            i = int(i)
            numbers.append(i)
    elif 'Remove' in command:
        command.pop(0)
        for i in command:
            i = int(i)
            numbers.remove(i)
    elif 'Replace' in command:
        command.pop(0)
        old_value = int(command[0])
        new_value = int(command[1])
        if old_value in numbers:
            numbers[numbers.index(old_value)] = new_value
    elif 'Collapse' in command:
        command.pop(0)
        threshold = int(command[0])
        numbers[:] = [num for num in numbers if num >= threshold]

while True:
    command = input()
    if command == 'Finish':
        for i in numbers:
            print(i, end=" ")
        break
    else:
        command = command.split()
        commands(command)