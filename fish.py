from random import randint
def fishFight(a, b):
    downstream = []
    survivors = 0
    
    for size, direction in zip(a, b): #zip linkea los elementos del mismo index en una misma tupla y hace una lista de ellas en el orden original
        if direction == 1:
            downstream.append(size)
        else:
            while downstream:
                if downstream[-1] > size:
                    break
                else:
                    downstream.pop()
            else:
                survivors += 1
                
    return survivors + len(downstream)

a = []
b = []

for i in range(randint(1, 1000)): #lo hago más chico porque me da miedo que se tilde todo por saturar la RAM
    a.append(randint(0, 1000000000))
    b.append(randint(0, 1))

print(fishFight(a, b))

