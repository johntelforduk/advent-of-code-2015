# Solution to day 5 of AOC 2015, Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5

import re
import string


def is_nice1(check: str) -> bool:
    """Return true iff string is 'nice' using Part 1 rules."""

    # "It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements."
    if re.match('[a-z]*(ab|cd|pq|xy)[a-z]*', check) is not None:
        return False

    # "It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou."
    vowel_count = 0

    # "It contains at least one letter that appears twice in a row, like xx, abcdde (dd),
    # or aabbccdd (aa, bb, cc, or dd)."
    prev_letter = ''
    two_in_a_row = False

    for letter in check:
        if letter in 'aeiou':
            vowel_count += 1

        if letter == prev_letter:
            two_in_a_row = True

        prev_letter = letter

    return vowel_count >= 3 and two_in_a_row


def is_nice2(check: str) -> bool:
    """Return true iff string is 'nice' using Part 2 rules."""

    # "It contains a pair of any two letters that appears at least twice in the string without overlapping,
    # like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps)."

    rule1 = False
    for pair_pos in range(len(check) - 1):
        pair = check[pair_pos:pair_pos + 2]
        rest = check[pair_pos + 2:]
        if pair in rest:
            rule1 = True
            break

    # "It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe),
    # or even aaa."

    rule2 = False
    for letter in string.ascii_lowercase:               # Try every lowercase letter of the alphabet.
        test_regex = '[a-z]*(' + letter + ')[a-z](' + letter + ')[a-z]*'
        if re.match(test_regex, check) is not None:
            rule2 = True
            break

    return rule1 and rule2


def main():
    f = open('input.txt')
    whole_text = f.read()
    f.close()

    nice1, nice2 = 0, 0
    for candidate in whole_text.split():
        if is_nice1(candidate):
            nice1 += 1
        if is_nice2(candidate):
            nice2 += 1

    print('Part 1:', nice1)
    print('Part 2:', nice2)


if __name__ == "__main__":
    main()
