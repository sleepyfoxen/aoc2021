from collections import defaultdict

with open('/home/fox/aoc2021/inputs/day6', 'r') as f:
    in_ = list(map(int, f.read().strip().split(',')))

# in_ = list(map(int, '3,4,3,1,2'.split(',')))

d = defaultdict(int)
for fishies in in_: d[fishies] += 1


for i in range(256):
    if i == 80: print(sum(d.values()))
    for j, fishies in tuple(d.items()):
        if j == 0:
            d[6] += fishies
            d[8] += fishies
        else:
            d[j-1] += fishies

        d[j] -= fishies


print(sum(d.values()))
