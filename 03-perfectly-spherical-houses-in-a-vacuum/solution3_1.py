# Solution to part 1 of day 3 of AOC 2015, Perfectly Spherical Houses in a Vacuum.
# https://adventofcode.com/2015/day/3


f = open('input.txt')
moves = f.read()
f.close()

x_delta = {'^': 0, '>': 1, 'v': 0, '<': -1}
y_delta = {'^': -1, '>': 0, 'v': 1, '<': 0}

visited = set()

x, y = 0, 0                         # Santa's current location (x y).
visited.add((x, y))

for direction in moves:
    x += x_delta[direction]
    y += y_delta[direction]
    visited.add((x, y))

print('Part 1:', len(visited))
