text_seperated = {}

words_to_seperate = input().split(' ')

for word_in_list in words_to_seperate:
    for letter in word_in_list:
        if letter not in text_seperated:
            text_seperated[letter] = 1
        else:
            text_seperated[letter] += 1

for letter, times_used in text_seperated.items():
    print(f'{letter} -> {times_used}')