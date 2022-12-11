fin = open("input_11.txt").read().strip().split('\n')

class Monkey():
    def __init__(self, items, operation, testval, truetarget, falsetarget, group):
        self.items = items
        self.operation = operation
        self.testval = testval
        self.truetarget = truetarget
        self.falsetarget = falsetarget
        self.bcounter = 0
        self.group = group

    def business(self):
        for item in self.items:
            old = item
            new = eval(self.operation)
            new = new%magic
            if new%self.testval==0:
                self.group[self.truetarget].items.append(new)
            else:
                self.group[self.falsetarget].items.append(new)
            self.bcounter += 1
        self.items = []

monkey = []
magic = 1

for line in fin:
    if line.startswith("  Starting"):
        items = [int(x) for x in line.split(":")[1].split(',')]
    if line.startswith("  Operation"):
        operation = line.split('=')[1]
    if line.startswith("  Test"):
        testval = int(line.split()[-1])
        magic *= testval
    if "true" in line:
        truetarget = int(line.split()[-1])
    if "false" in line:
        falsetarget = int(line.split()[-1])
        monkey.append(Monkey(items, operation, testval, truetarget, falsetarget, monkey))

for _ in range(10000):
    for m in monkey:
        m.business()

counts = [m.bcounter for m in monkey]
counts.sort()
print(counts[-1]*counts[-2])
