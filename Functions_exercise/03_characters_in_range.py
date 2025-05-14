character1 = input()
character2 = input()

def characters_in_range(start: str, end: str) -> list:
    '''

    :param the first
    :param character2:
    :return:
    '''
    list_of_characters_in_between = list(chr(char) for char in range(ord(start) + 1, ord(end)))
    return ' '.join(list_of_characters_in_between)




print(characters_in_range(character1, character2))
