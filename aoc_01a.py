f = open('input_01.txt')

currentmax = 0
thiscount = 0

for line in f:
    line = line.strip()
    if line == '':
        if thiscount > currentmax:
            currentmax = thiscount
        thiscount = 0
    else:
        thiscount += int(line)

print(currentmax)


