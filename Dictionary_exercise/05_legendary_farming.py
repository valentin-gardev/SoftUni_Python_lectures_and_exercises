legendary = {'fragments': 'Valanyr', 'shards': 'Shadowmourne', 'motes': 'Dragonwrath'}
quantity_and_materials_input = input().split()



materials_and_quantity = {'shards': 0, 'fragments': 0, 'motes': 0}
while True:
    for imput in range(0, len(quantity_and_materials_input), 2):
        quantity = int(quantity_and_materials_input[imput])
        material_upper = quantity_and_materials_input[imput + 1]
        material = material_upper.lower()
        if material not in materials_and_quantity:
            materials_and_quantity[material] = quantity
        else:
            materials_and_quantity[material] += quantity
        if material in legendary:
            if materials_and_quantity.get(material) >= 250:
                materials_and_quantity[material] -= 250
                print(f'{legendary.get(material)} obtained!')
                legendary.pop(material)
                for item, quantity in materials_and_quantity.items():
                    print(f'{item}: {quantity}')
                break
    if len(legendary) < 3:
        break
    quantity_and_materials_input = input().split()



    # for check in legendary:
    #     if check in materials_and_quantity:
    #         if materials_and_quantity.get(check) >= 250:
    #             materials_and_quantity[check] -= 250



