goods = input().split()
bakery = {}
for i in range(0, len(goods), 2):
    item = goods[i]
    amount = goods[i + 1]
    bakery[item] = int(amount)

print(bakery)