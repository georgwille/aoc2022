f = open("input_07.txt").read().split("\n")

# node = {id : (parent-id, name, content = list-of-nodes-ids OR int}


def names_in_dir(id):
    return [tree[entry][1] for entry in tree[id][2]]


def sizeof(id):
    size = 0
    for node in tree[id][2]:
        if type(tree[node][2]) == list:
            size += sizeof(node)
        else:
            size += tree[node][2]
    return size


cur = newnum = 0
tree = {newnum: (0, "/", [])}
newnum += 1

for line in f:
    if line == "":
        break
    if line.startswith("$ cd"):
        dirname = line.split()[-1]
        if dirname == "..":
            cur = tree[cur][0]
        elif dirname == "/":
            cur = 0
        else:
            for id in tree[cur][2]:
                if tree[id][1] == dirname:
                    cur = id
    if line.startswith("$ ls"):
        continue
    if line.startswith("dir"):
        dirname = line.split()[-1]
        if dirname not in names_in_dir(cur):
            tree[newnum] = (cur, dirname, [])
            tree[cur][2].append(newnum)
            newnum += 1
    if line[0].isdigit():
        size, fname = line.split()
        if fname not in names_in_dir(cur):
            tree[newnum] = (cur, fname, int(size))
            tree[cur][2].append(newnum)
            newnum += 1

validcount = 0
best = sizeof(0)
free = 70000000 - best
needed = 30000000

for node in tree:
    if type(tree[node][2]) == list:
        size = sizeof(node)
        if size <= 100000:
            validcount += size
        if size + free >= needed and size < best:
            best = size

print(validcount)
print(best)
