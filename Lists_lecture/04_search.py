number = int(input())
word = input()
all_words = []
list_with_included_word = []
for _ in range(number):
    other_words = input()
    all_words.append(other_words)

for l in all_words:
    if word in l:
        list_with_included_word.append(l)

print(all_words)
print(list_with_included_word)