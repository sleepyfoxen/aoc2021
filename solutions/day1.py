
with open('/home/fox/aoc2021/inputs/day1', 'r') as f:
    in_ = map(int, f.read().strip().split('\n'))

# in_ = map(int, '''199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263'''.strip().split('\n'))

in_ = list(in_)
inc = 0
inc2 = 0


for (this, next_) in zip(in_, in_[1:]):
    if next_ > this:
        inc += 1

print(inc)

zip3 = list(zip(in_, in_[1:], in_[2:]))
for (this, next_) in zip(zip3, zip3[1:]):
    if sum(next_) > sum(this):
        inc2 += 1

print(inc2)
