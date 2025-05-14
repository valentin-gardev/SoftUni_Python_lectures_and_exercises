number = int(input())

for num in range(1 ,number + 1):
    digits = num
    sum_numbers = 0

    while digits > 0:
        sum_numbers += digits % 10
        digits = int(digits/10)

    if (sum_numbers == 5) or (sum_numbers == 7) or (sum_numbers == 11):
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

