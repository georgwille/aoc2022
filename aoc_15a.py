def xy_from_text(text):
    x_s = text.index('x')+2
    x_e = text.index(',')
    y_s = text.index('y')+2
    x = int(text[x_s:x_e])
    y = int(text[y_s:])
    return (x,y)

def man(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

# fin = open("input_15_sample.txt").read().strip().split('\n')
# check_y = 10
fin = open("input_15.txt").read().strip().split('\n')
check_y = 2000000

sb = {} # (x,y) sensor : (x,y) nearest beacon

for line in fin:
    left, right = line.split(':')
    sb[xy_from_text(left)] = xy_from_text(right)

count = 0
int_on_check_y = []
beacons_on_check_y = set()

for s,b in sb.items():
    if b[1] == check_y:
        beacons_on_check_y.add(b)
    dy = abs(check_y - s[1])
    dx = man(s,b) - dy
    if dx >= 0:
        int_on_check_y.append((s[0]-dx,s[0]+dx))


print(int_on_check_y)

testset = set()

# hideous abuse of memory... :(
for pair in int_on_check_y:
    testset.update(set(list(range(pair[0],pair[1]+1))))

print(len(testset)-len(beacons_on_check_y))

