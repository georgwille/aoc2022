fin = open("input_13.txt").read().strip().split('\n')
fin = [eval(line) for line in fin if line]

def compare(left,right):
    for itemleft, itemright in zip(left,right):
        tl = type(itemleft)
        tr = type(itemright)
        if tl == int and tr == int:
            if itemleft < itemright:
                return -1
            elif itemleft > itemright:
                return 1
            else:
                continue
        elif tl == list and tr == int:
            return compare(itemleft,[itemright])
        elif tl == int and tr == list:
            return compare([itemleft],itemright)
        elif tl == list and tr == list:
            temp = compare(itemleft,itemright)
            if temp == 0:
                continue
            else:
                return temp
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0

correctsum = 0

for i in range(0,len(fin),2):
    left = fin[i]
    right = fin[i+1]
    if compare(left,right) == -1:
        correctsum += i//2 + 1

print(correctsum)

sep1 = [[2]]
sep1index = 1

sep2 = [[6]]
sep2index = 2

for elem in fin:
    if compare(elem,sep1) == -1:
        sep1index += 1
        sep2index += 1
        continue
    if compare(elem,sep2) == -1:
        sep2index += 1

print(sep1index*sep2index)

# from functools import cmp_to_key
# fin.append(sep1)
# fin.append(sep2)
# fin.sort(key=cmp_to_key(compare))
# print((fin.index(sep1)+1)*(fin.index(sep2)+1))
