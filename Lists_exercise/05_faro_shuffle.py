cards = input().split()
shuffles = int(input())
half_split = len(cards) //  2
faro_shuffled_deck = []

for _ in range(shuffles):
    deck_1 = cards[:half_split]
    deck_2 = cards[half_split:]
    cards.clear()
    for card in range(half_split):
        cards.append(deck_1[card])
        cards.append(deck_2[card])
print(cards)



