fin = open("input_20.txt").read().strip().split('\n')

def solve(key,rounds):
    nlist = [int(x)*key for x in fin]
    ll = len(nlist)-1
    ilist = list(range(ll+1))

    for _ in range(rounds):
        for i in range(ll+1):
            idx = ilist.index(i)
            ilist.pop(idx)
            ilist.insert((nlist[i]+idx)%ll,i)

    zidx = ilist.index(nlist.index(0))
    return sum(nlist[ilist[(zidx+k*1000)%(ll+1)]] for k in [1,2,3])


print(solve(1,1))
print(solve(811589153,10))
