
with open('/home/fox/aoc2021/inputs/day4', 'r') as f:
    in_ = f.read().strip().split('\n\n')

# in_ = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7'''.strip().split('\n\n')

draws = in_[0].strip()
boards = list(map(lambda t: t.split('\n'), in_[1:]))
boards = [ list(map(lambda t_:
                        t_.strip().replace('  ', ' ').split(' '), t))
                        for t in boards ]

boards_ = boards.copy()
b = False
res = 0

for draw in draws.split(','):
    for board in boards:
        for i in range(len(board)):
            row = board[i]
            if draw in row:
                row[row.index(draw)] = f'*{draw}'
        
        for row in board:
            if all(['*' in t for t in row]):
                b = True
                break

        for col in map(list, zip(*board)):
            if all(['*' in t for t in col]):
                b = True
                break
        
        if b:
            for row in board:
                res += sum(map(int, [e for e in row if '*' not in e]))
            print(res, draw, res*int(draw))
            break

    if b: break

# just restart for part 2
boards = boards_
b = False
res = 0
winners = []

for draw in draws.split(','):
    for boardidx in range(len(boards)):
        if boardidx in winners: continue
        board = boards[boardidx]
        for i in range(len(board)):
            row = board[i]
            if draw in row:
                row[row.index(draw)] = f'*{draw}'
        
        for row in board:
            if all(['*' in t for t in row]):
                b = True
                break

        for col in map(list, zip(*board)):
            if all(['*' in t for t in col]):
                b = True
                break
        
        if b:
            winners.append(boardidx)

            if len(winners) == len(boards):
                for row in board:
                    res += sum(map(int,
                                    [e for e in row if '*' not in e]))

                print(res, draw, res*int(draw))

            else:
                b = False

    if b: break
