fin = open("input_18.txt").read().strip().split()

field = set()

for line in fin:
    x,y,z = [int(a) for a in line.split(',')]
    field.add((x,y,z))


def neighbors_of(coord):
    cx, cy, cz = coord
    cand = [(cx-1,cy,cz),
            (cx+1,cy,cz),
            (cx,cy-1,cz),
            (cx,cy+1,cz),
            (cx,cy,cz-1),
            (cx,cy,cz+1)]
    return [el for el in cand if el in field]

surface = sum(6-len(neighbors_of(el)) for el in field)
print(surface)
