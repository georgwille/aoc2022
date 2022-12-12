# recycled and adapted from 2021/15
import heapq

with open('input_12.txt') as fin:
    m = {}
    for x,line in enumerate(fin):
        for y,char in enumerate(line.strip()):
            if char == "S":
                m[(x,y)]=0
                start = (x,y)
            elif char == "E":
                m[(x,y)]=25
                target = (x,y)
            else:
                m[(x,y)] = ord(char)-97

xmax = x
ymax = y

# here comes a cheap implementation of A*

openlist = {start:[0, None]} #   (x,y): [cost to here, parent]
closedlist = {} #                (x,y): [cost to here, parent]
olheap = []
heapq.heappush(olheap, [0,start])

while openlist:
    while True:
        current = heapq.heappop(olheap)[1]
        if current in openlist:
            break

    closedlist[current] = openlist.pop(current)

    if current == target:
        print(closedlist[current][0])
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        xn = current[0]+dx
        yn = current[1]+dy
        if not (0<=xn<=xmax and 0<=yn<=ymax):
            continue
        if (xn,yn) in closedlist:
            continue
        if m[xn,yn]-m[current] > 1:
            thiscost = 10000
        else:
            thiscost = closedlist[current][0]+1
        if (xn,yn) in openlist and thiscost >= openlist[(xn,yn)][0]:
            continue
        openlist[(xn,yn)] = [thiscost, current]
        heapq.heappush(olheap,[thiscost-xn-yn,(xn,yn)])
