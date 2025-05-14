order_numbers = int(input())
all_total = 0
for _ in range(order_numbers):
    total = 0
    price = float(input())
    days = int(input())
    needed_per_day = int(input())
    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= needed_per_day <= 2000:
        total = price * days * needed_per_day
        print(f"The price for the coffee is: ${total:.2f}")
        all_total += total
        continue
    else:
        continue
print(f"Total: ${all_total:.2f}")