# Solution to part 2 of day 12 of AOC 2015, JSAbacusFramework.io
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
            if type(d[k]) == str and d[k] == 'red':     # Special rule for Part 2.
                return 0
            total += sum_nums(d[k])
        return total

    else:
        return 0


assert sum_nums([1, 2, 3]) == 6
assert sum_nums([1,{"c":"red","b":2},3]) == 4
assert sum_nums({"d":"red","e":[1,2,3,4],"f":5}) == 0
assert sum_nums([1,"red",5]) == 6

f = open('input.txt')
whole_text = f.read()
f.close()

j = json.loads(whole_text)

print(sum_nums(j))
