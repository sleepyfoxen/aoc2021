

with open('/home/fox/aoc2021/inputs/day8', 'r') as f:
    in_ = f.read().strip().split('\n')

# in_ = '''
# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
# '''.strip().split('\n')

count = 0
for line in in_:
    _, outs = line.split(' | ')
    for t in outs.split(' '):
        if len(t) in (2, 3, 4, 7):
            count += 1

print(count)


b = { 2: [ 1 ],  # number of segments lit up -> possible digits
      3: [ 7 ],
      4: [ 4 ],
      5: [ 2, 3, 5 ],
      6: [ 0, 6, 9 ],
      7: [ 8 ] }

d = { (5, 3, 3, 4, 2): 2,   # magic tuples for 5- and 6-segment numbers
      (5, 2, 2, 3, 1): 3,
      (5, 3, 2, 4, 1): 5,   # tuples of the form (·, -7, -4, -1, -7-4)
      (6, 3, 3, 4, 2): 0,   #  representing the number of segments left
      (6, 4, 3, 5, 2): 6,   #  after removing ("subtracting") segments
      (6, 3, 2, 4, 1): 9 }  #  in ·, 7, 4, 1, and 7-4. [· = nothing]

result = 0
for line in in_:
    digits = [None] * 10  # tracks digits we know

    sigs, outs = line.split(' | ')
    sigs, outs = (it.split(' ') for it in (sigs, outs))

    # solve unambiguous-by-length digits (1, 4, 7, 8)
    for i, s in enumerate(sigs):
        sl = len(s)
        sd = b[sl]
        if len(sd) == 1: digits[sd[0]] = s

    # use solved digits to disambiguate the rest
    one, four, seven = ( frozenset(digits[i]) for i in (1, 4, 7) )
    for i, s in enumerate(sigs):
        if s in digits: continue
        ss = set(s)  # to use set difference

        magic = tuple(len(i) for i in
              (ss, ss - seven, ss - four, ss - one, ss - seven - four))
        digits[d[magic]] = s

    # decode output digits
    tmp = ( i for o in outs
                  for i, dd in enumerate(digits) if set(o) == set(dd) )
    out = int(''.join(map(str, tmp)))
    result += out

print(result)
