numbers = input().split()
def rounded(numbers):
    rounded_num = []
    for i in numbers:
        round_num = round(float(i))
        rounded_num.append(round_num)
    return rounded_num

print(rounded(numbers))