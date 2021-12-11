
with open('/home/fox/aoc2021/inputs/day9', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678'''.strip().split('\n')

in_ = [ [ int(c) for c in cs ] for cs in in_ ]
lowpoints = dict()

for y, line in enumerate(in_):
    for x, c in enumerate(line):
        # search for a lower point nearby
        for (y_, x_) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            y_, x_ = y + y_, x + x_
            if y_ < 0 or x_ < 0:                    continue
            if y_ >= len(in_) or x_ >= len(in_[y]): continue

            c_ = in_[y_][x_]  # bounds checked
            if c >= c_: break

        # lower point not found
        else: lowpoints[y, x] = c

print(sum(i+1 for i in lowpoints.values()))


def g(y, x):
    cyclers = (-1, 0), (1, 0), (0, -1), (0, 1)
    nine = [ False ] * 4
    scale = 1
    while True:
        for i, (dy, dx) in enumerate(cyclers):
            dy, dx = dy*scale, dx*scale
            y_, x_ = y + dy, x + dx
            if nine[i] or (y_, x_) in gs:           continue  # bounds
            if y_ < 0 or x_ < 0:                    continue
            if y_ >= len(in_) or x_ >= len(in_[y]): continue

            p = in_[y_][x_]   # safe
            if p == 9:  nine[i] = True
            else:       yield y_, x_
        
        if True in nine: return
        scale += 1

gs = dict()
blen = []
for y, x in lowpoints.keys():
    basin, basin_last = set(), 0
    basin.add((y, x))
    g_ = g(y, x)
    gs[y, x] = g_
    for p in g_: basin.add(p)

    while not len(basin) == basin_last:
        basin_last = len(basin)
        for (y_, x_) in (p for p in frozenset(basin) if p not in gs):
            g_ = g(y_, x_)
            gs[y_, x_] = g_
            for p in g_: basin.add(p)

    blen.append(len(basin))

blen = sorted(blen)
print(blen[-1] * blen[-2] * blen[-3])
