qmap, ins = open("input_22.txt").read().split('\n\n')
edgelength = int(((qmap.count('.')+qmap.count('#')+1)//6)**0.5)

qmap = qmap.split('\n')
mlength = max(len(line) for line in qmap)

for l,line in enumerate(qmap):
    qmap[l]=' '+line+' '*(mlength-len(line)+1)

qmap.insert(0," "*(mlength+2))
qmap.append(" "*(mlength+2))

pos = (1,qmap[1].find('.'))
dirs = {(0,1):0,(0,-1):2,(-1,0):3,(1,0):1} # r,l,u,d
drx = (0,1) # initial direction is right
# [print(line) for line in map]

def transform(pos,drx):
    row,col = pos
    while qmap[row][col] == ' ':
        col = (col-1+drx[1])%mlength+1
        row = (row-1+drx[0])%(len(qmap)-2)+1
    return (row,col),drx


i_pointer = 0

while True:
    if i_pointer == -1:
        break
    if ins[i_pointer] == 'L':
        drx = - drx[1], drx[0]
        i_pointer += 1
        continue
    elif ins[i_pointer] == 'R':
        drx = drx[1], -drx[0]
        i_pointer += 1
        continue
    else:
        next_t_pointer = ins.replace('L','R').find('R',i_pointer)
        count = int(ins[i_pointer:next_t_pointer])
        i_pointer = next_t_pointer
    for _ in range(count):
        npos = pos[0]+drx[0],pos[1]+drx[1]
        if qmap[npos[0]][npos[1]]==' ':
            npos,drx = transform(npos,drx)
        if qmap[npos[0]][npos[1]]=='.':
            pos = npos
            continue
        elif qmap[npos[0]][npos[1]]=='#':
            break

print(pos[0]*1000+pos[1]*4+dirs[drx])