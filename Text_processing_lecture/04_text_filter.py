banned_words = input().split(', ')
received_text = input()

for ban_word in banned_words:
    received_text = received_text.replace(ban_word, '*' * len(ban_word))

print(received_text)