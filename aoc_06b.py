f = open("input_06.txt").read().strip()

l = 14

for i in range(len(f)):
    if len(set(list(f[i:i+l]))) == l:
        print(i+l,f[i:i+l])
        break
