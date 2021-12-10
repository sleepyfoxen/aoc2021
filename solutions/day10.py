
from statistics import median

with open('/home/fox/aoc2021/inputs/day10', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]'''.strip().split('\n')

closes = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

pens = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

pen = 0

discards = []
for i, line in enumerate(in_):
    stack = []

    for c in line:
        if c in '([{<':
            stack.append(c)
            continue

        expected = closes[stack[-1]]
        if c != expected:
            # print(f'expected {expected}, but found {c} instead')
            pen += pens[c]
            discards.append(i)
            break

        else:
            stack.pop()

print(pen)

sc_tab = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


scores = []
for i, line in enumerate(in_):
    if i in discards: continue

    stack = []
    score = 0

    for c in line:
        if c in '([{<':
            stack.append(c)
            continue

        else:
            stack.pop()
    
    remain = ''.join(map(lambda a: closes[a], stack[::-1]))
    
    for c in remain:
        score *= 5
        score += sc_tab[c]
    
    scores.append(score)

print(median(scores))