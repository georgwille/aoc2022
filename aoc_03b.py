f = open('input_03.txt').read().split()

total = 0

for ii in range(0,len(f),3):
    c1, c2, c3 = [set(f[ii+o]) for o in [0,1,2]]
    e = list(c1.intersection(c2).intersection(c3))
    a = ord(e[0])
    total += a-38 if a < 91 else a-96

print(total)
