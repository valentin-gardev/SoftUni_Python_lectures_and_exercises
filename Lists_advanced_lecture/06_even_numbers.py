# numbers = list(map(int, input().split(', '))) # the easy way I found to solve this one
# even_numbers = list(filter(lambda index: numbers[index] % 2 == 0, range(len(numbers))))
# print(even_numbers)
# number_list = list(map(int, input().split(', ')))# Code from the lecture
# found_indices_or_no = list(map(
#     lambda x: x if number_list[x] % 2 == 0 else 'no',
#     range(len(number_list)))
# )
# print(found_indices_or_no)
# print(number_list)
# even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))
# print(even_indices)