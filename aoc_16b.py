fin = open("input_16.txt").read().strip().split('\n')

valves = set()
cvalves = set()
flow_rate = {} # valve:flow rate
conns = {} # valve: list of connecting valves

for line in fin:
    items = line.split()
    valve = items[1]
    valves.add(valve)
    flow_rate[valve] = int(items[4].split('=')[1][:-1])
    if flow_rate[valve] > 0:
        cvalves.add(valve)
    conns[valve] = [x.replace(',','') for x in items[9:]]

DONE={}

def search(pos, closed_valves, time_remaining, elephant=False):
    state = (pos, tuple(closed_valves),time_remaining,elephant)
    if state in DONE:
        return DONE[state]
    if time_remaining == 0:
        return 0
    score_do_nothing = 0
    score_open_this = 0
    score_elephant = 0
    # If I stopped here, what score could the elephant get with the valves that are still open?
    # if not elephant:
    if not elephant and len(closed_valves) < 9: # a bit crude, but it works: much faster
        score_elephant = search('AA', closed_valves.copy(), 26, elephant=True)
    # do nothing
    if time_remaining and closed_valves:
        score_do_nothing = max(search(conn, closed_valves.copy(), time_remaining-1, elephant) for conn in conns[pos])
    # open this valve
    if pos in closed_valves:
        time_remaining -= 1
        score_open_this = time_remaining * flow_rate[pos]
        closed_valves.discard(pos)
        if time_remaining and closed_valves:
            score_open_this += max(search(conn, closed_valves.copy(), time_remaining-1, elephant) for conn in conns[pos])
    score = max(score_do_nothing, score_open_this, score_elephant)
    DONE[state] = score
    return score

print(search('AA',cvalves,26))
