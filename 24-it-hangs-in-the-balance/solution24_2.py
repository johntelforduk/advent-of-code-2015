# Solution to part 2 of day 24 of AOC 2015, It Hangs in the Balance
# https://adventofcode.com/2015/day/24

from itertools import combinations


def product(s: list) -> int:
    """Return product of integers in parm list."""
    x = 1
    for i in s:
        x *= i
    return x


assert product([1, 2, 3, 4]) == 24


def find_solutions(packages_left: list, t: int, group_no: int) -> int:
    if group_no == 4:
        return 1

    lowest = None
    tuple_length = 1

    while lowest is None and tuple_length < len(packages_left) + 1:
        # print(f'tuple_length={tuple_length}')

        for combo in combinations(packages_left, tuple_length):
            combo_list = list(combo)
            if sum(combo_list) == t:
                next_packages_left = packages_left.copy()

                for each_package in combo_list:
                    next_packages_left.remove(each_package)

                # print(f'Checking next group of packages_left={next_packages_left}')

                if find_solutions(packages_left=next_packages_left, t=t, group_no=group_no + 1) is not None:
                    e = product(s=combo_list)
                    if lowest is None or e < lowest:
                        lowest = e

        tuple_length += 1
    return lowest


f = open('input.txt')
whole_text = f.read()
f.close()

packages = [int(each) for each in whole_text.split('\n')]
target = sum(packages) // 4
print(f'packages={packages}, target={target}')

solution = find_solutions(packages_left=packages, t=target, group_no=1)
print(f'solution={solution}')
