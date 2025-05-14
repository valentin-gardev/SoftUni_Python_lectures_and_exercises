energy = 100
coins = 100

work_day_list = input().split('|')
def rest(еnergy, event):
    global energy
    event = event.split('-')
    gained_energy = int(event[1])
    if energy + gained_energy <= 100:
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f'Current energy: {energy}.')
    elif energy + gained_energy > 100:
        gained_energy = 100 - energy
        energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f'Current energy: {energy}.')

def order(event):
    global coins
    global energy
    event = event.split('-')
    if energy - 30 < 0:
        energy += 50
        print(f'You had to rest!')
    else:
        coins += int(event[1])
        energy -= 30
        print(f'You earned {event[1]} coins.')

def buying_ingredient(event):
    global coins
    event = event.split('-')
    ingredient = event[0]
    if coins - int(event[1]) < 0:
        print(f'Closed! Cannot afford {ingredient}.')
        return False
    else:
        coins -= int(event[1])
        print(f'You bought {ingredient}.')
        return True



def events(work_day_list):

    for event in work_day_list:
        if 'rest' in event:
            rest(energy, event)
        elif 'order' in event:
            order(event)
        else:
            if not buying_ingredient(event):
                break

    else:
        print(f'Day completed!')
        print(f'Coins: {coins}')
        print(f'Energy: {energy}')

events(work_day_list)