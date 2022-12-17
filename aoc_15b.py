def xy_from_text(text):
    x_s = text.index('x')+2
    x_e = text.index(',')
    y_s = text.index('y')+2
    x = int(text[x_s:x_e])
    y = int(text[y_s:])
    return (x,y)

# fin = open("input_15_sample.txt").read().strip().split('\n')
# check_y = 10
fin = open("input_15.txt").read().strip().split('\n')

sb = {} # (x,y) sensor : (x,y) nearest beacon

for line in fin:
    left, right = line.split(':')
    sb[xy_from_text(left)] = xy_from_text(right)

# strategy: find all intersections of sensor edge neighbors
# within the given field (0 <= x,y <= 4000000)
# because that must be where the hidden beacon is
# BUT ONLY IF there is really just one!
# test those candidates whether they are inside
# another sensor range

def man(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def is_in_some_range(coord):
    for s,b in sb.items():
        if man(s,coord) <= man(s,b):
            return True
    return False

def is_valid(coord):
    for i in [0,1]:
        if coord[i] < 0 or coord[i] > 4000000:
            return False
    return True

def line_intersection(a1,a2,b1,b2):
    ma = (a2[1]-a1[1])//(a2[0]-a1[0])
    na = a2[1] - ma*a2[0]
    mb = (b2[1]-b1[1])//(b2[0]-b1[0])
    nb = b2[1] - mb*b2[0]
    if (nb-na) % 2 == 1:
        return None
    xc = (nb-na) // (ma-mb)
    yc = ma*xc+na
    return (xc,yc)


def edge_intersections(s1,be1,s2,be2):
    intersections = []
    m1 = man(s1,be1)+1
    m2 = man(s2,be2)+1
    l1 = (s1[0]-m1, s1[1])
    r1 = (s1[0]+m1, s1[1])
    u1 = (s1[0], s1[1]+m1)
    d1 = (s1[0], s1[1]-m1)
    l2 = (s2[0]-m2, s2[1])
    r2 = (s2[0]+m2, s2[1])
    u2 = (s2[0], s2[1]+m2)
    d2 = (s2[0], s2[1]-m2)
    crossings = [(l1,u1,r2,u2),
                 (l1,u1,l2,d2),
                 (r1,d1,r2,u2),
                 (r1,d1,l2,d2),
                 (l1,d1,l2,u2),
                 (l1,d1,r2,d2),
                 (r1,u1,l2,u2),
                 (r1,u1,r2,d2)]
    for corners in crossings:
        cross = line_intersection(*corners)
        if cross:
            intersections.append(cross)
    return intersections

lsb = list(sb.keys())
found = False

for i,s1 in enumerate(lsb[:-1]):
    for j,s2 in enumerate(lsb[i+1:]):
        intersections = edge_intersections(s1,sb[s1],s2,sb[s2])
        for cand in intersections:
            if is_valid(cand):
                if not is_in_some_range(cand):
                    print(cand[0],cand[1],cand[0]*4000000+cand[1])
                    found = True
                    break
        if found: break
    if found: break
