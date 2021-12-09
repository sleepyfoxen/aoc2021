
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
        minadj = 0

        # search for a lower point nearby
        for (y_, x_) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            y_, x_ = y + y_, x + x_
            if y_ < 0 or x_ < 0 or y_ >= len(in_) or x_ >= len(in_[y]):
                continue

            c_ = in_[y_][x_]
            if c >= c_:  break

        # not found
        else: lowpoints[y, x] = c

print(sum(i+1 for i in lowpoints.values()))


def g(y, x):
    cyclers = (-1, 0), (1, 0), (0, -1), (0, 1)
    nine = [ False ] * 4
    scale = 1
    while True:
        spoken = False
        for i, (dy, dx) in enumerate(cyclers):
            if nine[i]: continue
            dy, dx = dy*scale, dx*scale
            y_, x_ = y + dy, x + dx

            if y_ < 0 or x_ < 0 or y_ >= len(in_) or x_ >= len(in_[y]):
                continue

            p = in_[y_][x_]
            if p == 9:
                nine[i] = True
                continue

            spoken = True
            yield y_, x_
        
        if not spoken: return
        scale += 1

gs = dict()

blen = []
for y, x in lowpoints.keys():
    basin, basin_last = set(), None
    basin.add((y, x))
    g_ = g(y, x)
    for p in g_: basin.add(p)

    while not basin == basin_last:
        basin_last = basin.copy()
        for (y_, x_) in basin_last:
            try: g_ = gs[(y_, x_)]
            except KeyError:
                g_ = g(y_, x_)
                gs[(y_, x_)] = g_

            for p in g_: basin.add(p)

    blen.append(len(basin))

blen = sorted(blen)
print(blen[-1] * blen[-2] * blen[-3])
