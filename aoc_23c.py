fin = open("input_23.txt").read().split()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
checkdir = {(-1, 0):((-1,-1),(-1,0),(-1,1)),
            ( 1, 0):((1,-1),(1,0),(1,1)),
            (0, -1):((-1,-1),(0,-1),(1,-1)),
            (0,  1):((-1,1),(0,1),(1,1))}
curdir = 0

elves = set()
for row, line in enumerate(fin):
    for col, char in enumerate(line):
        if char == '#':
            elves.add((row, col))


def has_no_neighbors(pos):
    c = sum((pos[0]+dr, pos[1]+dc) in elves for dc in [-1, 0, 1]
            for dr in [-1, 0, 1])
    return c == 1

def dir_is_clear(pos,dir_):
    for test in checkdir[dir_]:
        if (pos[0]+test[0],pos[1]+test[1]) in elves:
            return False
    return True

def elves_range():
    rowmin = min(elf[0] for elf in elves)
    rowmax = max(elf[0] for elf in elves)
    colmin = min(elf[1] for elf in elves)
    colmax = max(elf[1] for elf in elves)
    return rowmin, rowmax, colmin, colmax

def print_elves():
    rowmin, rowmax, colmin, colmax = elves_range()
    for r in range(rowmin,rowmax+1):
        for c in range(colmin,colmax+1):
            if (r,c) in elves:
                print('#',end='')
            else:
                print('.',end='')
        print()

haschanged = True
cyclecount = 0

while haschanged:
    haschanged = False
    prop_pos = {}
    for elf in elves:
        if has_no_neighbors(elf):
            continue
        for dircount in range(4):
            propdir = dirs[(curdir+dircount)%4]
            if dir_is_clear(elf, propdir):
                new_pos = elf[0]+propdir[0],elf[1]+propdir[1]
                if new_pos in prop_pos:
                    prop_pos[new_pos].append(elf)
                else:
                    prop_pos[new_pos]=[elf]
                break
    for new_p,ori in prop_pos.items():
        if len(ori) == 1:
            elves.remove(ori[0])
            elves.add(new_p)
            haschanged = True
    cyclecount += 1
    curdir += 1
    curdir %= 4
    if cyclecount == 10:
        rowmin, rowmax, colmin, colmax = elves_range()
        print((rowmax-rowmin+1)*(colmax-colmin+1)-len(elves))

print(cyclecount)
