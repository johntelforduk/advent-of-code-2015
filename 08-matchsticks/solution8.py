# Solution to day 8 of AOC 2015, Matchsticks
# https://adventofcode.com/2015/day/8

f = open('input.txt')
whole_text = f.read()
f.close()

total_chars, in_memory, extras = 0, 0, 0
for line in whole_text.split('\n'):
    print('line: ', line)
    total_chars += len(line)

    actual = eval(line)
    print('actual: ', actual)

    in_memory += len(actual)

    extras += 2 + line.count('\\') + line.count('"')

print('total_chars: ', total_chars)
print('in_memory: ', in_memory)
print('part 1: ', total_chars - in_memory)
print('part 2: ', extras)
