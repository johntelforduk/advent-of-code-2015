# Solution to day 11 of AOC 2015, Corporate Policy
# https://adventofcode.com/2015/day/11

import string


def contains(check: str, within: []) -> bool:
    """Returns True if any of the strings in the 'within' list is a substring of the 'check' string."""
    for w in within:
        if w in check:
            return True
    return False


def contains_2_doubles(check: str) -> bool:
    """Returns True if string contains at least two different, non-overlapping pairs of letters, like aa, bb, or zz"""
    found = 0
    for letter in string.ascii_lowercase:
        if (letter * 2) in check:
            found += 1
        if found == 2:
            return True
    return False


def increment(a: str) -> str:
    # Find first non-z character.
    for i in reversed(range(len(a))):
        # print(i)
        if a[i] != 'z':
            return a[:i] + chr(ord(a[i]) + 1) + 'a' * (len(a) - i - 1)


triples = []
for start in string.ascii_lowercase[:24]:
    # print(start)

    new_triple = ''
    for j in range(ord(start), ord(start) + 3):
        new_triple += chr(j)

    # print(new_triple)
    triples.append(new_triple)

# print('triples:', triples)

banned = ['i', 'o', 'l']

password = increment('vzbxxyzz')

# print('password, contains(password, triples):', password, contains(password, triples))
# print('password, not contains(password, banned):', password, not contains(password, banned))
# print('password, contains_2_doubles(password:', password, contains_2_doubles(password))

while not contains(password, triples) or contains(password, banned) or not contains_2_doubles(password):
    # print(password)
    password = increment(password)

print('password:', password)
