item_price_quantity = {}

item_input = input().split()

while item_input[0] != 'buy':
    item = item_input[0]
    price = float(item_input[1])
    quantity = int(item_input[2])
    if item not in item_price_quantity:
        item_price_quantity[item] = [price, quantity]
    else:
        item_price_quantity[item][0] = price
        item_price_quantity[item][1] += quantity
    item_input = input().split()

for item, price_quantity in item_price_quantity.items():
    print(f'{item} -> {(price_quantity[0] * price_quantity[1]):.2f}')