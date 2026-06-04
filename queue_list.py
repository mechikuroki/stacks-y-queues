from random import randint
queue = []
n = randint(1, 10)

for _ in range(n):
    queue.append(randint(1, 20)) # "enqueue"

for _ in range(randint(1, n)):
    queue.pop(0) # "dequeue"

print("Final queue:", queue)
