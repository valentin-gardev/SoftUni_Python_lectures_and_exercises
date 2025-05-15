words = input().split()
palindrome = input()
palindrome_count = 0
only_palindromes = []

for word in words:
    if palindrome == word:
        palindrome_count += 1

    if word == ''.join(reversed(word)):
        only_palindromes.append(word)

print(only_palindromes)
print(f'Found palindrome {palindrome_count} times')
