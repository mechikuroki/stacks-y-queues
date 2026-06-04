#este es el ejercicio 1, hice el 2do primero para poder usar el modelito que hice
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    def peek(self):
        try:
            print(self.stack[-1])
        except:
            print("Your stack is empty.")
    def size(self):
        print(len(self.stack))

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(3)
    stack.pop()
    stack.push(2)
    stack.push(8)
    stack.pop()
    stack.pop()
    stack.push(9)
    stack.push(1)
    stack.pop()
    stack.push(7)
    stack.push(6)
    stack.pop()
    stack.push(4)
    stack.pop()
    stack.pop()
    
    for i in reversed(stack.stack):
        print(i)

