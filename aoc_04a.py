fin = open('input_04.txt').read().split()

contained = 0

for line in fin:
    p1, p2 = line.split(',')
    l1,l2 = p1.split('-')
    r1,r2 = p2.split('-')
    l1,l2,r1,r2 = int(l1), int(l2), int(r1), int(r2)
    if (l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2):
        contained += 1

print(contained)
