
def price_order(item, amount):
    if item == 'coffee':
        price = 1.50
    elif item == 'water':
        price = 1.00
    elif item == 'coke':
        price = 1.40
    elif item == 'snacks':
        price = 2.00
    return price * amount






item = input()
amount = int(input())

print(f'{price_order(item, amount):.2f}')