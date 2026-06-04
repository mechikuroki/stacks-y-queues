from random import randint
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        try:
            self.stack.pop()
        except:
            print("Your stack is empty.")
    def peek(self):
        try:
            print(self.stack[-1])
        except:
            print("Your stack is empty.")
    def size(self):
        print(len(self.stack))

def transfer(s, t):
    for _ in range(len(t.stack)):
        s.stack.append(t.stack.pop())

s = Stack()
t = Stack()

for i in range(randint(1, 10)):
    s.push(i)

for i in range(randint(1, 10)):
    t.push(i)


transfer(s, t)

for i in s.stack:
    print(i)

