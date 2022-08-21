# Solution to part 1 of day 24 of AOC 2015, It Hangs in the Balance
# https://adventofcode.com/2015/day/24

from itertools import combinations


def product(s: list) -> int:
    """Return product of integers in parm list."""
    x = 1
    for i in s:
        x *= i
    return x


assert product([1, 2, 3, 4]) == 24


def can_make_target(p: list, t: int) -> bool:
    """Can the parm list of packages p, be added up in any way to make target sum t?"""
    if t == 0:
        return True
    if len(p) == 0:
        return False
    if min(p) > t:
        return False

    for i in p:
        new_p = p.copy()
        new_p.remove(i)
        if can_make_target(new_p, t - i):
            return True
    return False


assert can_make_target([1, 2, 3], 1)
assert can_make_target([1, 2, 3], 3)
assert can_make_target([1, 2, 3], 5)
assert can_make_target([1, 2, 3], 6)
assert not can_make_target([], 5)
assert not can_make_target([1, 2, 3], 7)


f = open('input.txt')
whole_text = f.read()
f.close()

packages = [int(each) for each in whole_text.split('\n')]
target = sum(packages) // 3
print(f'packages={packages}, target={target}')

lowest = None
tuple_length = 1
while lowest is None and tuple_length < len(packages) + 1:
    print(f'tuple_length={tuple_length}')

    for combo in combinations(packages, tuple_length):
        combo_list = list(combo)
        if sum(combo_list) == target:
            packages_left = packages.copy()

            for each_package in combo_list:
                packages_left.remove(each_package)

            print(f'checking packages_left={packages_left}')

            if can_make_target(p=packages_left, t=target):
                e = product(s=combo_list)
                if lowest is None or e < lowest:
                    lowest = e

    tuple_length += 1

print(f'lowest={lowest}')
