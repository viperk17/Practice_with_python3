import random as r

# val = r.randint(0,10)
# print(val)

# 1 deck of cards
deck = list(range(1, 53))

hand = r.sample(deck, k=5)

# r.shuffle(deck)
print(hand)
