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


def print_chamber():
    for y in range(highest + 8, -1, -1):
        for x in range(7):
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


wind_d = wind_gen()
tilesource = tile_gen()

for tilecount in range(2022):

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
