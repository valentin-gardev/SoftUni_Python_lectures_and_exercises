
list_parts = []
for i in range(3):
    body_parts = input()
    list_parts.append(body_parts)

list_parts[0], list_parts[2] = list_parts[2], list_parts[0]
print(list_parts)