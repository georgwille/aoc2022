import heapq

mazestart = open("input_24.txt").read().strip().split()

mazestart = mazestart[1:-1]

mazestart = [line[1:-1] for line in mazestart]

nrows = len(mazestart)
ncols = len(mazestart[0])

startpos = (-1, 0, 0)
endpos = (nrows-1, ncols-1)


def maze_free(r, c, t):
    if (r, c) == (-1, 0):
        return True
    if mazestart[r][(c-t) % ncols] == '>':
        return False
    if mazestart[r][(c+t) % ncols] == '<':
        return False
    if mazestart[(r-t) % nrows][c] == "v":
        return False
    if mazestart[(r+t) % nrows][c] == "^":
        return False
    return True


# A* yet again, a bit modified

openlist = {startpos: [0, None]}  # (x,y): [cost to here, parent]
closedlist = {}  # (x,y): [cost to here, parent]
olheap = []
heapq.heappush(olheap, [0, startpos])

while openlist:
    while True:
        current = heapq.heappop(olheap)[1]
        if current in openlist:
            break

    closedlist[current] = openlist.pop(current)

    if current[:2] == endpos:
        print(current, closedlist[current][0]+1)
        # while closedlist[current][0]:
        #     print(current,closedlist[current][0])
        #     current = closedlist[current][1]
        break

    for dr, dc, dt in [(-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1), (0, 0, 1)]:
        rn = current[0]+dr
        cn = current[1]+dc
        tn = current[2]+dt
        if not ((0 <= cn < ncols and 0 <= rn < nrows) or (rn, cn) == startpos[:2]):
            continue
        if not maze_free(rn, cn, tn):
            continue
        if (rn, cn, tn) in closedlist:
            continue
        else:
            thiscost = closedlist[current][0]+1
        if (rn, cn, tn) in openlist and thiscost >= openlist[(rn, cn, tn)][0]:
            continue
        openlist[(rn, cn, tn)] = [thiscost, current]
        heapq.heappush(olheap, [thiscost-cn-rn, (rn, cn, tn)])
