money_as_string = input().split(", ")   #My conclution
beggars_count = int(input())
what_beggars_take_home = []

for beggar in range(beggars_count):
    num = 0
    for i in range(beggar, len(money_as_string) , beggars_count):
        num += int(money_as_string[i])
    what_beggars_take_home.append(num)

print(what_beggars_take_home)

