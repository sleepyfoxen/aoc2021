
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
    if dir_ == 'forward': hor += int(amount)
    if dir_ == 'backward': hor -= int(amount)
    if dir_ == 'down': ver += int(amount)
    if dir_ == 'up': ver -= int(amount)

print(hor, ver, hor*ver)

hor = 0
ver = 0
aim = 0

for line in in_:
    dir_, amount = line.split(' ')
    if dir_ == 'forward':
        hor += int(amount)
        ver += aim * int(amount)
    if dir_ == 'backward':
        hor -= int(amount)
        ver -= aim * int(amount)
    if dir_ == 'down': aim += int(amount)
    if dir_ == 'up': aim -= int(amount)

print(hor, ver, hor*ver)
