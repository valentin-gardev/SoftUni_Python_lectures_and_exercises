def even_num(num):

    return num % 2 != 0


sequence_of_numbers = list(map(int, input().split()))
even_numbers = filter(even_num, sequence_of_numbers)
print(list(even_numbers))