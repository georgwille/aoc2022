fin = open("input_13.txt").read().strip().split('\n')
fin = [eval(line) for line in fin if line]

def compare(left,right):
    for itemleft, itemright in zip(left,right):
        # print()
        # print(itemleft)
        # print(itemright)
        tl = type(itemleft)
        tr = type(itemright)
        if tl == int and tr == int:
            if itemleft < itemright:
                return True
            elif itemleft > itemright:
                return False
            else:
                continue
        elif tl == list and tr == int:
            return compare(itemleft,[itemright])
        elif tl == int and tr == list:
            return compare([itemleft],itemright)
        elif tl == list and tr == list:
            temp = compare(itemleft,itemright)
            if temp == "Proceed":
                continue
            else:
                return temp
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return "Proceed"

correctsum = 0

for i in range(0,len(fin),2):
    left = fin[i]
    right = fin[i+1]
    # print(left)
    # print(right)
    result = compare(left,right)
    # print(result)
    if result:
        correctsum += i//2 + 1

print(correctsum)
