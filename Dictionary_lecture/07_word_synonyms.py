dictionary = {}
number_words = int(input())

for _ in range(number_words):
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = [synonym]
    else:
        dictionary[word].append(synonym)

for word, synonym in dictionary.items():
    print(f'{word} - {", ".join(synonym)}')

print(dictionary)
