from collections import deque
fin = open('input_19.txt')

class Recipe():
    def __init__(self, id_, or_o, cr_o, sr_o, sr_c, gr_o, gr_s):
        # o .. ore, c .. clay, s .. obsidian, g .. geodes
        self.id_ = id_
        self.or_o = or_o
        self.cr_o = cr_o
        self.sr_o = sr_o
        self.sr_c = sr_c
        self.gr_o = gr_o
        self.gr_s = gr_s

recipes = []
for line in fin:
    parts = line.split()
    r = Recipe(int(parts[1][:-1]),
               int(parts[6]),
               int(parts[12]),
               int(parts[18]),
               int(parts[21]),
               int(parts[27]),
               int(parts[30]))
    recipes.append(r)

def solve(r, o_r, c_r, s_r, g_r, o, c, s, g, t):
    max_geodes = 0
    state = (o_r, c_r, s_r, g_r, o, c, s, g, t)
    max_ore_cost = max(r.gr_o, r.cr_o, r.sr_o, r.gr_o)
    TODO = deque()
    TODO.append(state)
    DONE = set()
    while TODO:
        this_state = TODO.pop()
        if this_state in DONE:
            continue
        o_r, c_r, s_r, g_r, o, c, s, g, t = this_state

        if t == 0:
            continue

        # cap all resources to what could possibly be needed until the end,
        # otherwise these variable numbers bloat the state space

        # cap ore
        o = min(o, t*max_ore_cost - o_r*(t-1))

        # cap clay
        c = min(c, t*r.sr_c - c_r*(t-1))

        # cap obsidian
        s = min(s, t*r.gr_s - s_r*(t-1))

        DONE.add(this_state)
        # if g == max_geodes:
        #     print(this_state)

        # geode robots - always produce
        if o >= r.gr_o and s >= r.gr_s:
            TODO.append((o_r, c_r, s_r, g_r+1, o+o_r-r.gr_o, c+c_r, s+s_r-r.gr_s, g+g_r, t-1))

        # obsidian robots
        if o >= r.sr_o and c >= r.sr_c and s_r < r.gr_s:
            TODO.append((o_r, c_r, s_r+1, g_r, o+o_r-r.sr_o, c+c_r-r.sr_c, s+s_r, g+g_r, t-1))

        # clay robots
        if o >= r.cr_o and c_r < r.sr_c:
            TODO.append((o_r, c_r+1, s_r, g_r, o+o_r-r.cr_o, c+c_r, s+s_r, g+g_r, t-1))

        # ore robots
        if o >= r.or_o and o_r < max_ore_cost:
            TODO.append((o_r+1, c_r, s_r, g_r, o+o_r-r.or_o, c+c_r, s+s_r, g+g_r, t-1))

        # only collect resources
        TODO.append((o_r, c_r, s_r, g_r, o+o_r, c+c_r, s+s_r, g+g_r, t-1))

        max_geodes = max(max_geodes, g+g_r)

    return max_geodes


total = 1

for r in recipes[:3]:
    result = solve(r,1,0,0,0,0,0,0,0,32)
    print(r.id_, result)
    total *= result

print(total)