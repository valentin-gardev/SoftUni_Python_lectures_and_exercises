characters = input().split(', ')
character_dictionary = {char: ord(char) for char in characters}
print(character_dictionary)