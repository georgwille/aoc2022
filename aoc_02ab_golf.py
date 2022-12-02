s='417852396312456897'
p=[ord(l[0])+3*ord(l[2])-329 for l in open('i')]
t=[sum(int(s[e+o])for e in p)for o in [0,9]]
print(t)