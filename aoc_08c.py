import numpy as np

f = open("input_08.txt").read().split()
s = len(f)
forest = np.zeros((s,s))

for y,line in enumerate(f):
    for x,tree in enumerate(line):
        forest[x,y] = int(tree)

def isvisible(x,y):
    h = forest[x,y]
    if (forest[:x,y]<h).all(): return True
    if (forest[x+1:,y]<h).all(): return True
    if (forest[x,:y]<h).all(): return True
    if (forest[x,y+1:]<h).all(): return True
    return False

print(sum(isvisible(x,y) for x in range(s) for y in range(s)))

def visscore(x,y):
    h = forest[x,y]
    view_xr = 1+np.argwhere(forest[x+1:,y]>=h)[0][0]
    view_xl = x-np.argwhere(forest[:x,y]>=h)[-1][0]
    view_yr = 1+np.argwhere(forest[x,y+1:]>=h)[0][0]
    view_yl = y-np.argwhere(forest[x,:y]>=h)[-1][0]
    return view_xr*view_xl*view_yr*view_yl

forest[(0,s-1),:]=99
forest[:,(0,s-1)]=99

print(max(visscore(x,y) for x in range(1,s-1) for y in range(1,s-1)))
