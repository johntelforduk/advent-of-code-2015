# Solution to day 8 of AOC 2015, Infinite Elves and Infinite Houses
# https://adventofcode.com/2015/day/20

from random import randint

def factors(x: int) -> list:
    f = []
    for t in range(1, 1 + x):
        if x % t == 0:
            f.append(t)
    return f

def presents(x: int) -> int:
    p = 0
    for f in factors(x):
        p += 10 * f
    return p

puzzle_input = 34000000

best = None


while True:
    attempt, p = 1, 0
    while p < puzzle_input:
        m = randint(1, 15)
        attempt *= m
        p = presents(attempt)
    if best is None or attempt < best:
        best = attempt
        print('best, p, puzzle_input:', best, p, puzzle_input)
