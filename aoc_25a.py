fin = open("input_25.txt").read().strip().split()

translate={'=':-2,'-':-1,'0':0,'1':1,'2':2}
revtrans ={-2:'=',-1:'-',0:'0',1:'1',2:'2'}

total = 0
for line in fin:
    ex = 0
    for char in line[::-1]:
        total += translate[char]*5**ex
        ex += 1

digits = ''

while total > 0:
    cand = total%5
    if cand > 2:
        cand -= 5
        total += 5
    total //= 5
    digits = revtrans[cand] + digits

print(digits)
