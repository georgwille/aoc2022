import time, sys
from importlib import reload

try:
    num = sys.argv[1]
except:
    print("Specify file, e.g. 9a, 10b, 11c, or full file name")
    print("Optional 2nd parameter is number of rounds")
    sys.exit()

if num.endswith('.py'):
    num = num[:-3]

if len(num)<4 and num[0].isdigit() and num[-1] in ('abcdef'):
    command = f'reload(aoc_{num:0>3})'
    scommand = f'import aoc_{num:0>3}'
else:
    command = f'reload({num})'
    scommand = f'import {num}'

runtimes = []

try:
    rounds = int(sys.argv[2])
except:
    rounds = 20

print("Discarding startup round")
exec(scommand)
print("Startup round discarded\n")

for _ in range(rounds):
    starttime = time.perf_counter()
    exec(command)
    runtime = time.perf_counter()-starttime
    # print(f"{runtime:.6f}")
    runtimes.append(runtime)

print(f"Minimum of {rounds} rounds: {min(runtimes):.6f}")
