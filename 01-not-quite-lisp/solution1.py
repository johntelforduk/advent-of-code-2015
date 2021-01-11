# Solution to day 1 of AOC 2015, Not Quite Lisp.
# https://adventofcode.com/2015/day/1


f = open('input.txt')
whole_text = f.read()
f.close()

floor = 0
steps = 0
basement_found = False

for each_char in whole_text:
    if not basement_found:
        steps += 1
    if each_char == '(':
        floor += 1
    elif each_char == ')':
        floor -= 1
    if floor == -1:
        basement_found = True

print('Part 1:', floor)
print('Part 2:', steps)
