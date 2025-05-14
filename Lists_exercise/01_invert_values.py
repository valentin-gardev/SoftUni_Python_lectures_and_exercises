numbers = input()

list_numbers = numbers.split(" ")
list_reversed = []

for i in list_numbers:
    i = int(i)
    i = i * -1
    list_reversed.append(i)

print(list_reversed)