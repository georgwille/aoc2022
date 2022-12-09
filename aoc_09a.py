fin = open("input_09_sample.txt").read().strip().split("\n")

h = [0,0]
t = [0,0]

maxd = 1

tailvisit = []

tmove = [[( 1,-1),( 1,-1),( 0,-1),(-1,-1),(-1,-1)],
         [( 1,-1),( 0, 0),( 0, 0),( 0, 0),(-1,-1)],
         [( 1, 0),( 0, 0),( 0, 0),( 0, 0),(-1, 0)],
         [( 1, 1),( 0, 0),( 0, 0),( 0, 0),(-1, 1)],
         [( 1, 1),( 1, 1),( 0, 1),(-1, 1),(-1, 1)]]

dirs = {"U":(0,1), "D":(0,-1), "R":(1,0), "L": (-1,0)}

for line in fin:
    d, count = line.split()
    count = int(count)
    for _ in range(count):
        h[0] += dirs[d][0]
        h[1] += dirs[d][1]
        tx = t[0]-tmove[h[1]-t[1]+2][h[0]-t[0]+2][0]
        ty = t[1]+tmove[h[1]-t[1]+2][h[0]-t[0]+2][1]
        t[0],t[1] = tx,ty
        tailvisit.append((t[0],t[1]))

print(len(set(tailvisit)))
