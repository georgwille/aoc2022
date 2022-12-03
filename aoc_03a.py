f = open('input_03.txt').read().split()

total = 0

for line in f:
    h = len(line)//2
    c1 = set(line[:h])
    c2 = set(line[h:])
    e = list(c1.intersection(c2))
    a = ord(e[0])
    total += a-38 if a < 91 else a-96

print(total)
