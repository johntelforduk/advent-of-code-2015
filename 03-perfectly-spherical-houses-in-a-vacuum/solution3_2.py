# Solution to part 2 of day 3 of AOC 2015, Perfectly Spherical Houses in a Vacuum.
# https://adventofcode.com/2015/day/3


f = open('input.txt')
moves = f.read()
f.close()

x_delta = {'^': 0, '>': 1, 'v': 0, '<': -1}
y_delta = {'^': -1, '>': 0, 'v': 1, '<': 0}

visited = set()

x1, y1, x2, y2 = 0, 0, 0, 0         # Santa's location is (x1, y1). Robo-Santa is (x2, y2).
visited.add((x1, y1))

move_num = 0
for direction in moves:
    if (move_num % 2) == 0:
        x1 += x_delta[direction]
        y1 += y_delta[direction]
        visited.add((x1, y1))
    else:
        x2 += x_delta[direction]
        y2 += y_delta[direction]
        visited.add((x2, y2))

    move_num += 1

print('Part 2:', len(visited))
