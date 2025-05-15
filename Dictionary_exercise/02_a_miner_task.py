new_string = input()
lines = 0
list_resource = []
list_resource_amount = []
mine = {}
while new_string != 'stop':
    lines += 1
    if lines % 2 != 0:
        list_resource.append(new_string)
    else:
        list_resource_amount.append(int(new_string))
    new_string = input()

for resource, resource_amount in zip(list_resource, list_resource_amount):
    if resource not in mine:
        mine[resource] = resource_amount
    else:
        mine[resource] += resource_amount

for resources, amount in mine.items():
    print(f'{resources} -> {amount}')