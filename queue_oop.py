#esta es la versión con lista. usé una clase para poder usar 'push' y 'pop' como nombres de función
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        try:
            self.queue.pop(0)
        except:
            print("Your queue is empty.")
    def peek(self):
        try:
            print(self.queue[1])
        except:
            print("Your queue is empty.")
    def size(self):
        print(len(self.queue))

if __name__ == "__main__":
    queue = Queue()
    running = True

    while running:
        print()
        print("------------------------------------")
        print("This is your queue: <OUT> ", queue.queue, " <IN>")
        print("------------------------------------")
            
        print("Press 1 to enqueue an item")
        print("Press 2 to dequeue an item")
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
                    queue.enqueue(item)
            case '2':
                queue.dequeue()
            case '3':
                queue.peek()
            case '4':
                queue.size()
            case '5':
                running = False
            case _:
                print('Invalid input. Try again.')


 
