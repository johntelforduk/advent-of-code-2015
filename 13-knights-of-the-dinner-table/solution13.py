# Solution to day 13 of AOC 2015, Knights of the Dinner Table
# https://adventofcode.com/2015/day/13


from itertools import permutations


f = open('input_2.txt')
whole_text = f.read()
f.close()

people = set()
feelings = {}
for l in whole_text.split('\n'):
    # print(l)
    attendee, _, g_or_l, unit, _, _, _, _, _, _, neighbor = l.split()

    if g_or_l == 'gain':
        sign = 1
    else:
        sign = -1

    feelings[(attendee, neighbor.split('.')[0])] = sign * int(unit)

    people.add(attendee)

print('people, feelings:', people, feelings)

highest = None
for arrangement in permutations(people, len(people)):
    arrange_list = list(arrangement)
    # print('arrange_list:', arrange_list)

    this_score = 0
    for chair in range(len(arrange_list)):

        # Work out the positions of the 2 neighboring chairs.
        n1 = (chair - 1) % len(arrange_list)
        n2 = (chair + 1) % len(arrange_list)

        # print('chair, n1, n2:', chair, n1, n2)

        this_score += feelings[(arrange_list[chair], arrange_list[n1])]
        this_score += feelings[(arrange_list[chair], arrange_list[n2])]

    if highest is None:
        highest = this_score
    else:
        highest = max(highest, this_score)

print(highest)
