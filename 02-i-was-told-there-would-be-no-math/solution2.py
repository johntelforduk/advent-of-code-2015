# Solution to day 2 of AOC 2015, I Was Told There Would Be No Math.
# https://adventofcode.com/2015/day/2


f = open('input.txt')
whole_text = f.read()
f.close()

total_paper = 0
total_ribbon = 0
for raw_box in whole_text.split('\n'):
    [rl, rw, rh] = raw_box.split('x')
    r, w, h = int(rl), int(rw), int(rh)
    f1, f2, f3 = r * w, r * h, w * h

    smallest = min(f1, f2, f3)
    paper = 2 * (f1 + f2 + f3) + smallest
    total_paper += paper

    shortest = sorted([r, w, h])[0]
    middle = sorted([r, w, h])[1]
    volume = r * w * h

    ribbon = 2 * (shortest + middle) + volume
    total_ribbon += ribbon

print('Part 1:', total_paper)
print('Part 2:', total_ribbon)
