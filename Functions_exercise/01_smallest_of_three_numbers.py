def smallest_num(num_list):
    num_list.sort()
    return num_list[0]



num_list = []
for _ in range (3):
    num = int(input())
    num_list.append(num)


print(smallest_num(num_list))