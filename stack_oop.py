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

if __name__ == "__main__":
    stack = Stack()
    running = True

    while running:
        print()
        print("------------------------------------")
        print("This is your stack:")
            
        for i in reversed(stack.stack):    
            print(i)

        print("------------------------------------")
            
        print("Press 1 to push an item")
        print("Press 2 to pop an item")
        print("Press 3 to peek the top element")
        print("Press 4 to check size")
        print("Press 5 to exit")

        ans = input("What do you want to do?: ")

        print()

        match ans:
            case '1':
                try:
                    item = int(input("Write your item to insert: "))
                except:
                    print("Not added. Please only input natural numbers.")
                else:
                    stack.push(item)
            case '2':
                stack.pop()
            case '3':
                stack.peek()
            case '4':
                stack.size()
            case '5':
                running = False
            case _:
                print('Invalid input. Try again.')


 
