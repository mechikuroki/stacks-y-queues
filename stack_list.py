from random import randint
stack = []
n = randint(1, 10)

for _ in range(n):
    stack.append(randint(1, 20)) # "push"

for _ in range(randint(1, n)):
    stack.pop() # "pop"

print("Final stack:")
for i in reversed(stack):
    print(i)
