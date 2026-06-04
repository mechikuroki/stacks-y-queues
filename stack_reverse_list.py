from random import randint
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("Your stack is empty.")
    def peek(self):
        try:
            print(self.stack[-1])
        except:
            print("Your stack is empty.")
    def size(self):
        print(len(self.stack))


s = Stack()
t = []

for i in range(randint(1, 10)):
    t.append(i)

print(t)

for _ in range(len(t)):
    s.push(t.pop(0))
for _ in range(len(s.stack)):
    t.append(s.pop())


print(t)
