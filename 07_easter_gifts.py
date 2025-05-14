planned_gifts = input().split()

def outofstock(gift):
    for item_i in range(len(planned_gifts)):
        if planned_gifts[item_i] == gift:
            planned_gifts[item_i] = 'None'

def required(gift, index_gift):
    if index_gift < 0 or index_gift > len(planned_gifts):
        pass
    else:
        planned_gifts[index_gift] = gift


def justincase(gift):
    planned_gifts[-1] = gift



while True:
    command = input()
    if command == 'No Money':
        break
    elif 'OutOfStock' in command:
        gift = command.split()[1]
        outofstock(gift)
    elif 'Required' in command:
        gift = command.split()[1]
        index_gift = int(command.split()[2])
        required(gift, index_gift)
    elif 'JustInCase' in command:
        gift = command.split()[1]
        justincase(gift)

for gift in planned_gifts:
    if gift == 'None':
        continue
    else:
        print(gift, end=' ')