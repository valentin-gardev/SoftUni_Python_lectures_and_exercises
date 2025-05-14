word = input()
word_reversed = ""

for x in range(len(word) -1, -1, -1):
    word_reversed += word[x]

print(word_reversed)