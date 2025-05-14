number = int(input())

while True:
    number += 1
    number = str(number)
    if len(set(number)) == len(number):
        number = int(number)
        print(number)
        break
    else:
        number = int(number)