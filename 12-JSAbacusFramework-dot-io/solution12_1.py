# Solution to part 1 of day 12 of AOC 2015, JSAbacusFramework.io
# https://adventofcode.com/2015/day/12

import json


def sum_nums(d) -> int:
    """Return the sum of all integers in the parm dictionary."""
    if type(d) == int:
        return d

    elif type(d) == list:
        total = 0
        for i in d:
            total += sum_nums(i)
        return total

    elif type(d) == dict:
        total = 0
        for k in d:
            total += sum_nums(d[k])
        return total

    else:
        return 0


assert sum_nums([1, 2, 3]) == 6
assert sum_nums({"a": 2, "b": 4}) == 6
assert sum_nums([[[3]]]) == 3
assert sum_nums({"a": {"b": 4}, "c": -1}) == 3
assert sum_nums({"a": [-1, 1]}) == 0
assert sum_nums([-1, {"a": 1}]) == 0
assert sum_nums([]) == 0
assert sum_nums({}) == 0

f = open('input.txt')
whole_text = f.read()
f.close()

j = json.loads(whole_text)

print(sum_nums(j))
