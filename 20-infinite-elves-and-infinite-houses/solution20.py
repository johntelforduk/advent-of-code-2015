# Solution to day 20 of AOC 2015, Infinite Elves and Infinite Houses
# https://adventofcode.com/2015/day/20

import math

def factors(n: int) -> list:
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [int(n / d) for d in small_divisors if n != d * d]
    return small_divisors + large_divisors


def presents1(x: int) -> int:
    p = 0
    for f in factors(x):
        p += 10 * f
    return p


def presents2(x: int) -> int:
    p = 0
    for f in factors(x):
        if x <= f * 50:
            p += 11 * f
    return p


puzzle_input = 34000000

best = None

attempt = 786240
while presents2(attempt) < puzzle_input:
    attempt += 1
    if attempt % 100000 == 0:
        print(attempt)
print(attempt)
