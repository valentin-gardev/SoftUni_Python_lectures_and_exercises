products = {}
total_products = 0
quantity = 0
while True:

    item = input().split(': ')

    if item[0] == 'statistics':
        print(f'Products in stock:')
        for p, q in products.items():
            print(f'- {p}: {q}')

        print(f'Total Products: {total_products}\nTotal Quantity: {quantity}')
        break

    if item[0] in products.keys():
        products[item[0]] += int(item[1])
        quantity += int(item[1])

    else:
        products[item[0]] = int(item[1])
        total_products += 1
        quantity += int(item[1])
