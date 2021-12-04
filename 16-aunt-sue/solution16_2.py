# Solution for part 1 of day 16 of AOC 2015, Aunt Sue
# https://adventofcode.com/2015/day/16

def eq(x, y):
    return x == y


def lt(x, y):
    return x < y


def gt(x, y):
    return x > y


mfcsam = {'children': (eq, 3),
          'cats': (gt, 7),
          'samoyeds': (eq, 2),
          'pomeranians': (lt, 3),
          'akitas': (eq, 0),
          'vizslas': (eq, 0),
          'goldfish': (lt, 5),
          'trees': (gt, 3),
          'cars': (eq, 2),
          'perfumes': (eq, 1)}

f = open('input.txt')
t = f.read()
f.close()

# Example row,
# Sue 1: goldfish: 6, trees: 9, akitas: 0

sue_num, k, v = None, None, None
for sue in t.split('\n'):
    i = 0
    found = True                                    # Be +ve, assume that this is the Sue!
    for term in sue.split(' '):
        if i == 1:
            sue_num = int(term.split(':')[0])

        if i in [2, 4, 6]:
            k = term.split(':')[0]
        if i in [3, 5, 7]:
            v = int(term.split(',')[0])

            func, bound = mfcsam[k]
            if not func(v, bound):
                found = False
        i += 1

    if found:
        print(sue_num)
