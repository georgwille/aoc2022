from functools import cmp_to_key

fin = open("input_13.txt").read().strip().split('\n')
fin = [eval(line) for line in fin if line]

sep1 = [[2]]
sep2 = [[6]]

fin.append(sep1)
fin.append(sep2)

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

fin.sort(key=cmp_to_key(compare))
print((fin.index(sep1)+1)*(fin.index(sep2)+1))