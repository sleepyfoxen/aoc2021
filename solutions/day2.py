
with open('/home/fox/aoc2021/inputs/day2', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2'''.strip().split('\n')

hor = 0
ver = 0

for line in in_:
    dir_, amount = line.split(' ')
    amount = int(amount)
    if dir_ == 'forward':   hor += amount
    if dir_ == 'backward':  hor -= amount
    if dir_ == 'down':      ver += amount
    if dir_ == 'up':        ver -= amount

print(hor, ver, hor*ver)

hor = 0
ver = 0
aim = 0

for line in in_:
    dir_, amount = line.split(' ')
    amount = int(amount)
    if dir_ == 'forward':
        hor += amount
        ver += aim * amount
    if dir_ == 'backward':
        hor -= amount
        ver -= aim * amount
    if dir_ == 'down':  aim += amount
    if dir_ == 'up':    aim -= amount

print(hor, ver, hor*ver)
