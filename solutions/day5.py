from collections import defaultdict

with open('/home/fox/aoc2021/inputs/day5', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2'''.strip().split('\n')

d1 = defaultdict(lambda: defaultdict(int))
d2 = defaultdict(lambda: defaultdict(int))

def minmax(a, b):
    if a < b: return (a, b)
    return (b, a)

def count(d):
    c = 0
    for v in d.values():
        for v_ in v.values():
            if v_ > 1: c += 1
    return c


for line in in_:
    p1, p2 = line.split(' -> ')
    (x1, y1), (x2, y2) = p1.split(','), p2.split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if x1 == x2:
        y1, y2 = minmax(y1, y2)
        for p in range(y1, y2+1):
            d1[x1][p] += 1
            d2[x1][p] += 1
    
    elif y1 == y2:
        x1, x2 = minmax(x1, x2)
        for p in range(x1, x2+1):
            d1[p][y1] += 1
            d2[p][y1] += 1

    else:
        m = (y2 - y1) / (x2 - x1)  # like in heckin school
        p = x1, y1
        x1, x2 = minmax(x1, x2)
        for px in range(x1, x2+1):
            py = m * (px - p[0]) + p[1]
            d2[px][int(py)] += 1


print(count(d1))
print(count(d2))
