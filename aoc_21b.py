fin = open("input_21.txt").read().strip().split('\n')

instruction = {}
for line in fin:
    first,rest = line.split(':')
    instruction[first] = rest.strip()

def what_yells(monkey):
    this_instruction = instruction[monkey]
    if this_instruction.isdigit():
        return int(this_instruction)
    m1,op,m2 = this_instruction.split()
    op1=what_yells(m1)
    op2=what_yells(m2)
    if monkey == 'root':
        return (op1,op2)

    if op == "+":
        return op1+op2
    if op == "-":
        return op1-op2
    if op == "*":
        return op1*op2
    if op == "/":
        return op1/op2
    assert False

upper = 10**14
lower = 0

# assuming a monotonic relationship
while True:
    test=(upper+lower)//2
    instruction["humn"] = str(test)
    left,right = what_yells("root")
    # comparison might have to be flipped for
    # other inputs
    if left > right:
        lower = test
    else:
        upper = test
    if left == right:
        print(test)
        break
