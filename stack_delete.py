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

def delete(s):
    s.stack.pop()
    if len(s.stack) != 0:
        delete(s)

s = Stack()

for i in range(randint(1, 10)):
    s.push(i)

delete(s)

print(s.stack)


