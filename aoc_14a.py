fin = open("input_14.txt").read().strip().split("\n")
# fin = open("input_14_sample.txt").read().strip().split("\n")

cave = {}

def print_cave():
    lo_y = min(y for (x,y) in cave)
    hi_y = max(y for (x,y) in cave)
    lo_x = min(x for (x,y) in cave)
    hi_x = max(x for (x,y) in cave)    
    for y in range(lo_y,hi_y+1):
        for x in range(lo_x,hi_x+1):
            if (x,y) in cave:
                if cave[(x,y)] == 1:
                    print("#", end='')
                elif cave[(x,y)] == 2:
                    print('o', end='')
                elif cave[(x,y)] == 3:
                    print('x', end='')
            else:
                print(' ', end='')
        print()
    print()

for line in fin:
    seq = line.split(" -> ")
    corners = [(int(pair.split(',')[0]),
                int(pair.split(',')[1])) for pair in seq]
    for idx,(xc,yc) in enumerate(corners[1:],1):
        if xc == corners[idx-1][0]:
            d = yc-corners[idx-1][1]
            d = 1 if d>0 else -1
            for y in range(corners[idx-1][1],yc+d,d):
                cave[xc,y] = 1
        else:
            d = xc-corners[idx-1][0]
            d = 1 if d>0 else -1
            for x in range(corners[idx-1][0],xc+d,d):
                cave[x,yc] = 1

lo_y = min(y for (x,y) in cave)
hi_y = max(y for (x,y) in cave)
lo_x = min(x for (x,y) in cave)
hi_x = max(x for (x,y) in cave)

graincount = 0
overflow = False

while not overflow:
    grain_x = 500
    grain_y = 0
    is_moving = True
    while is_moving:
        cave[(grain_x,grain_y)] = 3
        # print_cave()
        if grain_y >= hi_y:
            overflow = True
            is_moving = False
            continue
        if (grain_x,grain_y+1) not in cave:
            cave.pop((grain_x,grain_y))
            grain_y += 1
        elif (grain_x-1,grain_y+1) not in cave:
            cave.pop((grain_x,grain_y))
            grain_x -= 1
            grain_y += 1
        elif (grain_x+1,grain_y+1) not in cave:
            cave.pop((grain_x,grain_y))
            grain_x += 1
            grain_y += 1
        else:
            cave[(grain_x, grain_y)] = 2
            graincount += 1
            is_moving = False

# print_cave()
print(graincount)