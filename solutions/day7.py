from statistics import median

with open('/home/fox/aoc2021/inputs/day7', 'r') as f:
    in_ = list(map(int, f.read().strip().split(',')))

# in_ = list(map(int, '''16,1,2,0,4,2,7,1,2,14'''.split(',')))

med = int(median(in_))
print(sum( abs(x - med) for x in in_ ))

minimum = 1e10
for i in range(min(in_), max(in_)):
    ks = ( abs(x - i) for x in in_ )
    Sk = sum( k + k**2 >> 1 for k in ks )
    if Sk < minimum: minimum = Sk

print(minimum)
