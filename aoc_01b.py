f = open('input_01.txt')

thiscount = 0
carried = []

for line in f:
    line = line.strip()
    if line == '':
        carried.append(thiscount)
        thiscount = 0
    else:
        thiscount += int(line)

carried.sort()
print(sum(carried[-3:]))


