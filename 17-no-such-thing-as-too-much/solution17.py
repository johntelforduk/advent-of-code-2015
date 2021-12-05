# Solution to day 17 of AOC 2015, No Such Thing as Too Much
# https://adventofcode.com/2015/day/17

f = open('input.txt')
t = f.read()
f.close()

solutions = set()


def decant(eggnog_left, empty_containers: [], full_containers: str):
    if eggnog_left == 0:
        # Sorted because order that the containers are filled up doesn't matter.
        solutions.add(''.join(sorted(full_containers)))
        return

    if len(empty_containers) == 0:
        return

    for container_num in range(len(empty_containers)):
        name, size = empty_containers[container_num]
        if size <= eggnog_left:
            one_away = empty_containers[:]
            one_away.pop(container_num)
            # print(one_away)
            decant(eggnog_left - size, one_away, full_containers + name)
    return


containers = []
i = 0
for c in t.split('\n'):
    # Tuple is (unique name for each container, it's size)
    containers.append((chr(97 + i), int(c)))
    i += 1

decant(150, containers, '')

print(solutions)
print('Part 1:', len(solutions))

min_length = len(min(solutions, key=len))
few_containers = {short for short in solutions if len(short) == min_length}
print('Part 2:', len(few_containers))
