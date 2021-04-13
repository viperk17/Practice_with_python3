# import random as r

# # val = r.randint(0,10)
# # print(val)

# # 1 deck of cards
# deck = list(range(1, 53))

# hand = r.sample(deck, k=5)

# # r.shuffle(deck)
# print(hand)


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") 
print(queue)
queue.append("Tomm") 
print(queue)
queue.popleft()
print(queue)

queue.popleft()
print(queue)