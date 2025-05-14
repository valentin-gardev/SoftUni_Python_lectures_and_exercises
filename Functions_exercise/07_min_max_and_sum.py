def minimum_number(list_numbers) -> int:
    return min(list_numbers)
def maximum_number(list_numbers) -> int:
    return max(list_numbers)
def sum_numbers(list_numbers) -> int:
    return sum(list_numbers)


sequence_numbers = list(map(int, input().split()))

print(f'The minimum number is {minimum_number(sequence_numbers)}')
print(f'The maximum number is {maximum_number(sequence_numbers)}')
print(f'The sum number is: {sum_numbers(sequence_numbers)}')