fin = open("input_20.txt").read().strip().split('\n')

nlist = [int(x)*811589153 for x in fin]
ll = len(nlist)-1
zkey = nlist.index(0)

ilist = [i for i in range(ll+1)]

# print(nlist)
# print(ilist)

for roundcount in range(10):
    for i in range(ll+1):
        idx = ilist.index(i)
        ilist.pop(idx)
        ilist.insert((nlist[i]+idx)%ll,i)

        # for idx in ilist:
        #     print(nlist[idx],end=" ")
        # print()

zidx = ilist.index(zkey)
# print(zidx)

print(sum([nlist[ilist[(zidx+k*1000)%(ll+1)]] for k in [1,2,3]]))



