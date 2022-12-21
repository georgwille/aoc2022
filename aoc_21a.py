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
    if op == "+":
        return op1+op2
    if op == "-":
        return op1-op2
    if op == "*":
        return op1*op2
    if op == "/":
        return op1/op2
    assert False

print(what_yells('root'))