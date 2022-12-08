import numpy as np

f = open("input_08.txt").read().split()
s = len(f)
forest = np.zeros((s,s))

for x,line in enumerate(f):
    for y,tree in enumerate(line):
        forest[x,y] = int(tree)

def visscore(x,y):
    h = forest[x,y]
    view_xr = 1+np.argwhere(forest[x+1:,y]>=h)[0][0]
    view_xl = x-np.argwhere(forest[:x,y]>=h)[-1][0]
    view_yr = 1+np.argwhere(forest[x,y+1:]>=h)[0][0]
    view_yl = y-np.argwhere(forest[x,:y]>=h)[-1][0]
    return view_xr*view_xl*view_yr*view_yl

vismax = 0
forest[(0,s-1),:]=99
forest[:,(0,s-1)]=99

for x in range(1,s-1):
    for y in range(1,s-1):
        v = visscore(x,y)
        if v > vismax:
            vismax = v

print(vismax)