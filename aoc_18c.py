fin = open("input_18.txt").read().strip().split()

field = set()
cmax = cmin = 0

for line in fin:
    x,y,z = [int(a) for a in line.split(',')]
    cmin = min(cmin,x,y,z)
    cmax = max(cmax,x,y,z)
    field.add((x,y,z))

cmin -= 1
cmax += 1

def neighbors_of(coord,volume):
    return [el for el in all_neighbors_of(coord) if el in volume]

def all_neighbors_of(coord):
    cx, cy, cz = coord
    return [(cx - 1, cy, cz),
            (cx + 1, cy, cz),
            (cx, cy - 1, cz),
            (cx, cy + 1, cz),
            (cx, cy, cz - 1),
            (cx, cy, cz + 1),]


def inside_allowed(coord):
    for ax in [0,1,2]:
        if coord[ax] < cmin or coord[ax] > cmax:
            return False
    return True

surface = sum(6-len(neighbors_of(el,field)) for el in field)
print("Total surface:", surface)

# this is sufficient
space = {(cmin,cmin,cmin)}

# this is faster (more safe starting points for filling)
for a in range(cmin,cmax+1):
    for b in range(cmin,cmax+1):
        space.add((a,b,cmin))
        space.add((a,b,cmax))
        space.add((a,cmin,b))
        space.add((a,cmax,b))
        space.add((cmin,a,b))
        space.add((cmax,a,b))

edge = space

while edge:
    fresh = set()
    for el in edge:
        all_n = all_neighbors_of(el)
        for n in all_n:
            if n in field:
                continue
            if n not in space and inside_allowed(n):
                fresh.add(n)
    space.update(fresh)
    edge = fresh

acc_surface = sum(6-len(neighbors_of(el,space)) for el in space)
print("Accessible surface:", acc_surface-6*(cmax-cmin+1)**2)
