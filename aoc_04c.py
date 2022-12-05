fin = open('input_04.txt').read().split()

overlap = 0
contained = 0

for line in fin:
    p1, p2 = line.split(',')
    l1,l2 = p1.split('-')
    r1,r2 = p2.split('-')
    l1,l2,r1,r2 = int(l1), int(l2), int(r1), int(r2)
    if (l1-r1)*(l2-r2)<=0:
        contained += 1
    if (r1-l2)*(r2-l1)<=0:
        overlap += 1    

print(contained, overlap)
