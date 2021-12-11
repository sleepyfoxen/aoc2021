from itertools import product

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
    if (y, x) in flashed:
        return
    
    for dy, dx in directions:
        y_, x_ = y + dy, x + dx
        if y_ < 0 or x_ < 0:                        continue  # bounds
        if y_ >= len(in_) or x_ >= len(in_[y_]):    continue

        c_ = in_[y_][x_]  # safe
        c_ += 1
        in_[y_][x_] = c_

    flashed.add((y, x))
    flashes += 1

for i in range(steps):
    flashed.clear()

    # start by just increasing everyone :)
    for y, line in enumerate(in_):
        for x, c in enumerate(line):
            c += 1
            in_[y][x] = c

    # sort out the glowey bois
    for _ in range(100):  # input size bounded 10x10
        b = True
        for y, line in enumerate(in_):
            for x, c in enumerate(line):
                if c > 9:
                    flash(y, x)
                    b = False
        if b: break

    # send the glowers to snooze
    for y, line in enumerate(in_):
        for x, c in enumerate(line):
            if c > 9:
                in_[y][x] = 0

    # for l in in_: print(''.join(str(c) for c in l))
    # print()

    if len(flashed) == 100:
        print(i + 1)
        break

    if i == 99:
        print(flashes)
