numbers = input().split()
numbers_removed = int(input())
int_list_numbers = []
list_biggest_numbers = []

for num in numbers:
    int_list_numbers.append(int(num))

for _ in range(numbers_removed):
    int_list_numbers.remove(min(int_list_numbers))

print(*int_list_numbers, sep=", ")