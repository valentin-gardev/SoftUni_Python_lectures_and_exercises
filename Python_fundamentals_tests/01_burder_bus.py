number_of_cities = int(input())
city_counter = 1
total_earnings = 0
total_profit = 0

def city_profit(earnings,expenses):
    if city_counter % 3 == 0 and city_counter % 5 == 0:
        return (earnings - (earnings * 0.1)) - expenses
    elif city_counter % 3 == 0:
        return earnings - (expenses + (expenses * 0.5))
    elif city_counter % 5 == 0:
        return (earnings - (earnings * 0.1)) - expenses

    else:
        return earnings - expenses





for city in range(number_of_cities):
    city_name = input()
    earnings = float(input())
    expenses = float(input())

    total_profit += city_profit(earnings,expenses)

    print(f'In {city_name} Burger Bus earned {city_profit(earnings,expenses):.2f} leva.')
    city_counter += 1

print(f'Burger Bus total profit: {total_profit:.2f} leva.')