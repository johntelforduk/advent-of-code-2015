# Solution to day 4 of AOC 2015, The Ideal Stocking Stuffer.
# https://adventofcode.com/2015/day/4


import hashlib

puzzle_input = 'bgvyzdsv'

required_zeroes = 6

number = 1

while True:
    candidate = puzzle_input + str(number)
    result = hashlib.md5(candidate.encode()).hexdigest()
    if result[0:required_zeroes] == '0' * required_zeroes:
        break
    number += 1

print('Part 1:', number)
