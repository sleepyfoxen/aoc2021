from itertools import chain, product

with open('/home/fox/aoc2021/inputs/day11', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526'''.strip().split('\n')

in_ = [ [ int(c) for c in cs ] for cs in in_ ]
directions = tuple(product((-1, 0, 1), repeat=2))

flashed = set()
flashes = 0
steps = 800

def flash(y, x):
    global flashes
    if (y, x) in flashed: return

    for dy, dx in directions:
        y_, x_ = y + dy, x + dx
        if y_ < 0 or x_ < 0:                        continue  # bounds
        if y_ >= len(in_) or x_ >= len(in_[y_]):    continue

        in_[y_][x_] += 1  # safe

    flashed.add((y, x))
    flashes += 1

for i in range(steps):
    flashed.clear()

    # start by just increasing everyone :)
    in_ = [ [ c + 1 for c in line ] for line in in_ ]

    # sort out the glowey bois
    for _ in range(100):  # input size bounded 10x10
        if not any(map(lambda c: c > 9, chain(*in_))): break
        for y, line in enumerate(in_):
            for x, c in enumerate(line):
                if c > 9:
                    flash(y, x)

    # send the glowers to snooze
    in_ = [ [ 0 if c > 9 else c for c in line ] for line in in_ ]

    # for l in in_: print(''.join(str(c) for c in l))
    # print()

    if len(flashed) == 100:
        print(i + 1)
        break

    if i == 99:
        print(flashes)
