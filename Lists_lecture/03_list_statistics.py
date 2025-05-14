amount = int(input())
lst_positive = []
lst_negative = []
sum_negative = 0
for _ in range(amount):
    numbers = int(input())
    if numbers >= 0:
        lst_positive.append(numbers)

    else:
        lst_negative.append(numbers)

print(lst_positive)
print(lst_negative)
print(f"Count of positives: {len(lst_positive)}")
print(f"Sum of negatives: {sum(lst_negative)}")
