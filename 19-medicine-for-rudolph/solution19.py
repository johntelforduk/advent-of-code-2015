# Solution to day 19 of AOC 2015, Medicine for Rudolph
# https://adventofcode.com/2015/day/19


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

def main():
    f = open('input.txt')
    whole_text = f.read()
    f.close()

    raw_replacements, start = whole_text.split('\n\n')
    print('start: ', start)
    replacements_list = raw_replacements.split('\n')
    replacements = []
    for rule in replacements_list:
        [f, t] = rule.split(' => ')
        replacements.append((f, t))
    print('replacements: ', replacements)

    could = set()
    for p in range(len(start)):
        print(possible_at_position(start, replacements, p, 1))
        could = could.union(possible_at_position(start, replacements, p, 1))
#        could += possible_at_position(start, replacements, p, 1)

        if p + 1 < len(start):
            could = could.union(possible_at_position(start, replacements, p, 2))

    print('could:', could)
    print(len(could))


if __name__ == "__main__":
    main()
