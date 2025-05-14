sum_even = 0
sum_odd = 0




def even_odd(number: str):
    global sum_odd
    global sum_even
    for num in range(len(number)):
        if int(number[num]) % 2 == 0:
            sum_even += int(number[num])
        elif int(number[num]) % 2 != 0:
            sum_odd += int(number[num])

def result(sum_even, sum_odd):
    return print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')

number = input()
even_odd(number)
result(sum_even, sum_odd)