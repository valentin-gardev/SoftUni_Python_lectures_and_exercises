sequence_upper = input().split()
sequece_lower = [x.lower() for x in sequence_upper]
dictionary = {}

for word in sequece_lower:
    if word not in dictionary.keys():
        dictionary[word] = 1
    else:
        dictionary[word] += 1

for word, num in dictionary.items():
    if num % 2 != 0:
        print(word, end=' ')


