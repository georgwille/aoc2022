code = open("input_10.txt").read().strip().split("\n")

clock_h = [0]
regx_h = [1]
regx = 1

for line in code:
    if line.startswith("noop"):
        clock_h.append(clock_h[-1]+1)
        regx_h.append(regx_h[-1])
    if line.startswith("addx"):
        inc = int(line.split()[1])
        clock_h.append(clock_h[-1]+1)
        regx_h.append(regx_h[-1])
        clock_h.append(clock_h[-1]+1)
        regx_h.append(regx_h[-1]+inc)

for counter in range(len(clock_h)):
    xpos = counter % 40
    if xpos == 0:
        print()
    if abs(regx_h[counter]-xpos)<2:
        print('#',end='')
    else:
        print(' ',end='')
