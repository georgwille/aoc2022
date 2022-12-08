import numpy as np

f = open("input_08.txt").read().split()

forest = np.zeros((99,99))

for y,line in enumerate(f):
    for x,tree in enumerate(line):
        forest[x,y] = int(tree)

def isvisible(x,y):
    h = forest[x,y]
    if (forest[:x,y]<h).all():
        return True
    if (forest[x+1:,y]<h).all():
        return True
    if (forest[x,:y]<h).all():
        return True
    if (forest[x,y+1:]<h).all():
        return True
    return False

viscounter = 0

for x in range(99):
    for y in range(99):
        if isvisible(x,y):
            viscounter += 1

print(viscounter)