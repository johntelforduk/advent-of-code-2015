# Solution for part 1 of day 16 of AOC 2015, Aunt Sue
# https://adventofcode.com/2015/day/16

mfcsam = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1}

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

            if v != mfcsam[k]:
                found = False
        i += 1

    if found:
        print(sue_num)
