wind = open("input_17.txt").readline().strip()

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

chamber = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
highest = 0


def wind_gen():
    i = 0
    while True:
        if wind[i] == "<":
            yield -1
        else:
            yield 1
        i += 1
        i %= len(wind)


def tile_gen():
    i = 0
    while True:
        yield shapes[i]
        i += 1
        i %= 5


def move_tile(tile, direction):
    return [(el[0] + direction[0], el[1] + direction[1]) for el in tile]


def print_chamber(top=20):
    for x in range(7):
        for y in range(highest + 8, highest + 8 - top - 1, -1):
            if (x, y) in chamber:
                print("#", end="")
            elif (x, y) in cur_tile:
                print("@", end="")
            else:
                print(".", end="")
        print()
    print("------------")


def overlap(tile):
    for el in tile:
        if el in chamber or el[0] < 0 or el[0] > 6:
            return True
    return False


def checksum(layers=1):
    c = 0
    for l in range(highest, highest - layers - 1, -1):
        for pos in range(7):
            c = c << 1
            c = c | ((pos, l) in chamber)
    return c


wind_d = wind_gen()
tilesource = tile_gen()

cycles = {}
all_checksums = {}

for m in range(1000):
    print("cycle:", m)
    for tilecount in range(5 * len(wind)):
        cur_tile = move_tile(next(tilesource), (2, highest + 4))
        falling = True

        while falling:
            # print_chamber()
            cur_wind = next(wind_d)
            cand = move_tile(cur_tile, (cur_wind, 0))
            if not overlap(cand):
                cur_tile = cand
            cand = move_tile(cur_tile, (0, -1))
            if overlap(cand):
                falling = False
                break
            else:
                cur_tile = cand

        chamber.update(cur_tile)
        highest = max(max([y for (x, y) in cur_tile]), highest)
        # print_chamber()
    print(highest)
    print_chamber(30)
    cs = checksum(30)
    cycles[m] = (highest, cs)
    if cs in all_checksums:
        print("cycle found")
        print(all_checksums[cs], m)
        print(cycles[all_checksums[cs]], cycles[m])
        # print(cycles)
        break
    else:
        all_checksums[cs] = m

# Doesn't give the complete solution
# I was too lazy and did the rest on paper
