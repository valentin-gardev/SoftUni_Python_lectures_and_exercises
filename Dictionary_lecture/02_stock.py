stock = input().split()
in_stock = input().split()
warehouse = {}

for i in range(0, len(stock), 2):
    item = stock[i]
    amount = int(stock[i + 1])
    warehouse[item] = amount

for check in in_stock:
    if check in warehouse.keys():
        print(f'We have {warehouse[check]} of {check} left')
    else:
        print(f"Sorry, we don't have {check}")
