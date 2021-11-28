# Solution to part 1 of day 15 of AOC 2015, Science for Hungry People
# https://adventofcode.com/2015/day/15

f = open('input.txt')
whole_text = f.read()
f.close()

ingredients = {}

# Example,
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
for ingredient in whole_text.split('\n'):
    raw_name, _, raw_cap, _, raw_d, _, raw_f, _, raw_t, _, raw_cal = ingredient.split(' ')

    name = raw_name[:-1]
    cap = int(raw_cap[:-1])
    d = int(raw_d[:-1])
    f = int(raw_f[:-1])
    t = int(raw_t[:-1])
    cal = int(raw_cal)
    print(name, cap, d, f, t, cal)

    # Calories omitted.
    ingredients[name] = [cap, d, f, t]

print(ingredients)

highest = 0

for f in range(101):
    for c in range(101):
        for b in range(101):
            s = 100 - f - c - b
            # print(f, c, b, s)

            if s >= 0:
                score = 1
                for i in range(len(ingredients['Butterscotch'])):
                    quality = f * ingredients['Frosting'][i] + c * ingredients['Candy'][i]   \
                              + b * ingredients['Butterscotch'][i] + s * ingredients['Sugar'][i]

                    if quality < 0:
                        quality = 0
                    score *= quality
                print(score)
                highest = max(highest, score)

print(highest)
