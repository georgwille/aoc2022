fin = open("input_09.txt").read().strip().split("\n")

def sgn(a):
    if not a: return 0
    return 1 if a>0 else -1

dirs = {"U":1j, "D":-1j, "R":1+0j, "L":-1+0j}

def tailvisit(chainlength):
    chain = [0+0j]*chainlength
    visited = {chain[-1]}
    for line in fin:
        d, count = line.split()
        count = int(count)
        for _ in range(count):
            chain[0] += dirs[d]
            for pos in range(1,len(chain)):
                h, t = chain[pos-1], chain[pos]
                if abs(h-t) < 1.5: break
                chain[pos] += sgn(int((h-t).real))+sgn(int((h-t).imag))*1j
            visited.add(chain[-1])
    return len(visited)

print(tailvisit(2))
print(tailvisit(10))
