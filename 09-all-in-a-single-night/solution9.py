# Solution to day 9 of AOC 2015, All in a Single Night
# https://adventofcode.com/2015/day/9

from itertools import permutations

f = open('input.txt')
whole_text = f.read()
f.close()

lines = [line for line in whole_text.split('\n')]
print('lines:', lines)

vertices = set()
distances = {}
for line in lines:
    terms = line.split()
    origin, _, destination, _, distance = terms
    distances[(origin, destination)] = int(distance)
    distances[(destination, origin)] = int(distance)
    vertices.add(origin)
    vertices.add(destination)

print('distances:', distances)
print('vertices:', vertices)

shortest = None
longest = None

for route in permutations(vertices, len(vertices)):
    this_distance = 0
    a = None
    for b in route:
#        print(b)
        if a is not None:
            this_distance += distances[(a, b)]
        a = b
    if shortest is None:
        shortest = this_distance
        longest = this_distance
    else:
        shortest = min(shortest, this_distance)
        longest = max(longest, this_distance)

print('Part 1:', shortest)
print('Part 2:', longest)