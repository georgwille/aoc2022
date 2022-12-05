f = open("input_05.txt")

field1 = [[], [], [], [], [], [], [], [], [], []]
field2 = [[], [], [], [], [], [], [], [], [], []]

for line in f:
    line = line.strip("\n")
    if not (line):
        break
    for i in range(1, 10):
        c = line[4 * i - 3]
        if c.isalpha():
            field1[i].insert(0, c)
            field2[i].insert(0, c)

for line in f:
    _, cnt, _, src, _, tar = line.split(" ")
    cnt, src, tar = int(cnt), int(src), int(tar)
    field1[tar] += field1[src][:-cnt-1:-1]
    field1[src] = field1[src][:-cnt]
    field2[tar] += field2[src][-cnt:]
    field2[src] = field2[src][:-cnt]

print(''.join([stack[-1] for stack in field1[1:]]))
print(''.join([stack[-1] for stack in field2[1:]]))
