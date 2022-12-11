fin = open("input_11.txt").read().strip().split('\n')

class Monkey():
    def __init__(self, items, operation, testval, truetarget, falsetarget):
        self.items = items
        self.operation = operation
        self.testval = testval
        self.truetarget = truetarget
        self.falsetarget = falsetarget
        self.bcounter = 0

    def business(self):
        for item in self.items:
            old = item
            new = eval(self.operation)
            new = new//3
            if new%self.testval==0:
                monkey[self.truetarget].items.append(new)
            else:
                monkey[self.falsetarget].items.append(new)
            self.bcounter += 1
        self.items = []

monkey = []

for line in fin:
    if line.startswith("  Starting"):
        items = [int(x) for x in line.split(":")[1].split(',')]
    if line.startswith("  Operation"):
        operation = line.split('=')[1]
    if line.startswith("  Test"):
        testval = int(line.split()[-1])
    if "true" in line:
        truetarget = int(line.split()[-1])
    if "false" in line:
        falsetarget = int(line.split()[-1])
        monkey.append(Monkey(items, operation, testval, truetarget, falsetarget))

for _ in range(20):
    for m in monkey:
        m.business()

counts = [m.bcounter for m in monkey]
counts.sort()
print(counts[-1]*counts[-2])