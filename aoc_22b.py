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

def show_map(pos,drx):
    dsymbol={(-1,0):'^',(1,0):'v',(0,-1):'<',(0,1):'>'}
    for r,row in enumerate(qmap):
        for c,char in enumerate(row):
            if r == pos[0] and c == pos[1]:
                print(dsymbol[drx],end='')
            else:
                print(char,end='')
        print()

            

def transform(pos,drx):
#   0 1 2
# 0   1122
#     1122
# 1   33
#     33
# 2 4455
#   4455
# 3 66
#   66
    row,col = pos # position outside the given map (" ")
    rrow = (row-1)%50 # relative position (0-49)
    rcol = (col-1)%50
    orow = row-drx[0] # position before overstepping
    ocol = col-drx[1]
    key_r = (orow-1)//50 # region-determining numbers
    key_c = (ocol-1)//50
    if   (key_r,key_c) == (0,1) and drx == (-1,0): # 1u
        return (3*50+rcol+1,50-rrow),(0,1)
    elif (key_r,key_c) == (0,2) and drx == (-1,0): # 2u
        return (3*50+rrow+1,0*50+rcol+1),(-1,0)
    elif (key_r,key_c) == (0,1) and drx == (0,-1): # 1l
        return (3*50-rrow,50-rcol),(0,1)
    elif (key_r,key_c) == (0,2) and drx == (0, 1): # 2r
        return (3*50-rrow,2*50-rcol),(0,-1)
    elif (key_r,key_c) == (0,2) and drx == ( 1,0): # 2d
        return (1*50+rcol+1,2*50-rrow),(0,-1)
    elif (key_r,key_c) == (1,1) and drx == (0,-1): # 3l
        return (3*50-rcol,0*50+rrow+1),( 1,0)
    elif (key_r,key_c) == (1,1) and drx == (0, 1): # 3r
        return (50-rcol,2*50+rrow+1),(-1,0)
    elif (key_r,key_c) == (2,0) and drx == (-1,0): # 4u
        return (1*50+rcol+1,2*50-rrow),(0,1)
    elif (key_r,key_c) == (2,0) and drx == (0,-1): # 4l
        return (50-rrow, 2*50-rcol),(0,1)
    elif (key_r,key_c) == (2,1) and drx == (0, 1): # 5r
        return (50-rrow, 3*50-rcol),(0,-1)
    elif (key_r,key_c) == (2,1) and drx == ( 1,0): # 5d
        return (3*50+rcol+1, 50-rrow),(0,-1)
    elif (key_r,key_c) == (3,0) and drx == (0,-1): # 6l
        return (50-rcol, 50+rrow+1),(1,0)
    elif (key_r,key_c) == (3,0) and drx == (0, 1): # 6r
        return (3*50-rcol, 50+rrow+1),(-1,0)
    elif (key_r,key_c) == (3,0) and drx == ( 1,0): # 6d
        return (0*50+rrow+1, 2*50+rcol+1),( 1,0)
    else:
        print(key_r,key_c,drx)
        assert False


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
        has_transformed = False
        npos = pos[0]+drx[0],pos[1]+drx[1]
        if qmap[npos[0]][npos[1]]==' ':
            # print("before transform")
            # show_map(pos,drx)
            # input()
            npos,ndrx = transform(npos,drx)
            has_transformed = True
        if qmap[npos[0]][npos[1]]=='.':
            pos = npos
            if has_transformed:
                drx = ndrx
                has_transformed = False
                # print("after transform")
                # has_transformed = False
                # show_map(pos,drx)
                # input()
            continue
        elif qmap[npos[0]][npos[1]]=='#':
            break

print(pos[0]*1000+pos[1]*4+dirs[drx])