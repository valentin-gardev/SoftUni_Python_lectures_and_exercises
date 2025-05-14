divisor = int(input())
boundary = int(input())


for number in range(boundary, 0, -1):
    if number % divisor == 0 and number > 0 and number <= boundary:
        print(number)
        break