
with open('/home/fox/aoc2021/inputs/day3', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010'''.strip().split('\n')


entries = len(in_)
gammas = [ 0 for c in in_[0] ]

for line in in_:
    for i, c in enumerate(line):
        if c == '1': gammas[i] += 1 

gamma = 0
for bit in gammas:
    gamma <<= 1
    if bit > entries / 2:
        gamma += 1

eps = (1 << len(in_[0])) - gamma - 1
print(eps, gamma, eps*gamma)


o2 = in_.copy()
co2 = in_.copy()

# oxygen, use most common, break ties to 1
for i, bit in enumerate(gammas):

    bit = 0
    for line in o2:
        if line[i] == '1': bit += 1
    
    if bit > len(o2) / 2: o2 = [ t for t in o2 if t[i] == '1' ]
    elif bit < len(o2) / 2: o2 = [ t for t in o2 if t[i] == '0' ]
    else: o2 = [ t for t in o2 if t[i] == '1' ]

    if len(o2) == 1: break


# co2, use least common, break ties to 0
for i, bit in enumerate(gammas):

    bit = 0
    for line in co2:
        if line[i] == '1': bit += 1

    if bit > len(co2) / 2: co2 = [ t for t in co2 if t[i] == '0' ]
    elif bit < len(co2) / 2: co2 = [ t for t in co2 if t[i] == '1' ]
    else: co2 = [ t for t in co2 if t[i] == '0' ]

    if len(co2) == 1: break

print(o2, co2, int(o2[0], 2) * int(co2[0], 2))
