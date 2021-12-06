from collections import defaultdict

with open('/home/fox/aoc2021/inputs/day6', 'r') as f:
    in_ = list(map(int, f.read().strip().split(',')))

# in_ = list(map(int, '3,4,3,1,2'.split(',')))

d = defaultdict(int)


for fish in in_:
    d[fish] += 1

for i in range(256):

    if i == 80: print(sum(d.values()))

    for j, fish in list(d.items()):
        if j == 0:
            d[6] += fish
            d[8] += fish
        else:
            d[j-1] += fish

        d[j] -= fish


print(sum(d.values()))
