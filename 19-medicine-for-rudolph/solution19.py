# Solution to day 19 of AOC 2015, Medicine for Rudolph
# https://adventofcode.com/2015/day/19

import re
from random import shuffle


def possible_replacements(r: list, molecule: str) -> list:
    """For parm list of rule tuples (from, to), and parm 'from' molecules, return list of possible replacements."""
    result = []
    for f, t in r:
        if f == molecule:
            result.append(t)
    return result


def replace(s: str, p: int, r: str, l: int) -> str:
    """For parm string s, at position p, replace l number of chars with string r."""
    before = s[0: p]
    after = s[p + l:]
    return before + r + after


def possible_at_position(s: str, r: list, p: int, l: int) -> set:
    """For parm string s, at position p for l len of chars, return the set of possible single replacements
    based on the the list r of replacement tuples."""
    molecule = s[p: p + l]
    possible = set()
    for t in possible_replacements(r, molecule):
        possible.add(replace(s, p, t, l))
    return possible


BEST = None
SHORTEST = None


def simplify(m: str, r: list, s: int):
    """For molecule m, search list of replacements r for simplifications (shorter moecules.
    Parm s is number of steps taken to produce the parm molecule."""
    global BEST, SHORTEST

    lm = len(m)
    if SHORTEST is None:
        SHORTEST = lm
    elif lm < SHORTEST:
        SHORTEST = lm
        print('SHORTEST, s:', SHORTEST, s)

    if BEST is not None:
        if s >= BEST:
            return

    if m == 'e':
        if BEST is None:
            BEST = s
        else:
            BEST = s
        print('BEST: ', BEST)
        return

    shuffle(r)
    for (f, t) in r:
        p = m.find(t)
        if p != -1:
            new = replace(m, p, f, len(t))
            simplify(new, r, s + 1)


def main():
    f = open('input.txt')
    whole_text = f.read()
    f.close()

    raw_replacements, target = whole_text.split('\n\n')
    print('target: ', target)
    replacements_list = raw_replacements.split('\n')
    replacements = []
    for rule in replacements_list:
        [f, t] = rule.split(' => ')
        replacements.append((f, t))
    print('replacements: ', replacements)

    # --------------- Part 1
    could = set()
    for p in range(len(target)):
        could = could.union(possible_at_position(target, replacements, p, 1))

        if p + 1 < len(target):
            could = could.union(possible_at_position(target, replacements, p, 2))

    print('part 1:', len(could))

    # --------------- Part 2
    simplify(target, replacements, 0)


if __name__ == "__main__":
    main()
