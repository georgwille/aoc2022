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

signal_strength = 0

for counter in range(20,len(clock_h),40):
    print(clock_h[counter],regx_h[counter])
    signal_strength += clock_h[counter]*regx_h[counter-1]

print(signal_strength)

