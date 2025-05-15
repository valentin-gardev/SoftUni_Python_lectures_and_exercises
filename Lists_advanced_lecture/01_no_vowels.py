text = input()
text_no_vowels = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(text_no_vowels))