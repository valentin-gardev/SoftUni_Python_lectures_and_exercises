list_of_cards = input().split(', ')

number_of_moves = int(input())

for _ in range(number_of_moves):
    command = input().split(', ')
    if 'Add' in command:
        command.pop(0)
        for i in command:
            if i in list_of_cards:
                print('Card is already in the deck')
            else:
                list_of_cards.append(i)
                print('Card successfully added')
    elif 'Remove' in command:
        command.pop(0)
        for i in command:
            if i not in list_of_cards:
                print('Card not found')
            else:
                list_of_cards.remove(i)
                print('Card successfully removed')
    elif 'Remove At' in command:
        command.pop(0)
        for i in command:
            index = int(i)
        if index < 0 or index > len(list_of_cards):
            print('Index out of range')
        else:
            list_of_cards.pop(index)
            print('Card successfully removed')
    elif 'Insert' in command:
        command.pop(0)
        index = int(command[0])
        card = command[1]
        if index < 0 or index > len(list_of_cards):
            print('Index out of range')
        elif card in list_of_cards:
            print('Card is already added')
        else:
            list_of_cards.insert(index, card)
            print('Card successfully added')


print(*list_of_cards, sep=', ')