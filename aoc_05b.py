f = open("input_05.txt")

field = [[], [], [], [], [], [], [], [], [], []]

for line in f:
    line = line.strip("\n")
    if not (line):
        break
    for i in range(1, 10):
        c = line[4 * i - 3]
        if c.isalpha():
            field[i].insert(0, c)

for line in f:
    _, cnt, _, src, _, tar = line.split(" ")
    cnt, src, tar = int(cnt), int(src), int(tar)
    field[tar] += field[src][-cnt:]
    field[src] = field[src][:-cnt]

for stack in field[1:]:
    print(stack[-1], end="")
