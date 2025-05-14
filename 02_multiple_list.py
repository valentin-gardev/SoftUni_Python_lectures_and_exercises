factor = int(input())
count = int(input())
stop_count = 0
final_num = 1
list = []

while True:
    if stop_count == count:
        print(list)
        break
    elif final_num % factor == 0:
        list.append(final_num)
        final_num += 1
        stop_count += 1
    else:
        final_num += 1


