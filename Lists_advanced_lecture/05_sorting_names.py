string_names = input().split(', ')

sorted_names = sorted(string_names, key=lambda x: (-len(x), x))

print(sorted_names)