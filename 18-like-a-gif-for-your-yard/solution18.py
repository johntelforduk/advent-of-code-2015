# Solution to day 18 of AOC 2015, Like a GIF For Your Yard
# https://adventofcode.com/2015/day/18

import pygame

f = open('input.txt')
t = f.read()
f.close()

lights = set()
filenames = []
scale = 5


def print_lights():
    for print_y in range(6):
        for print_x in range(6):
            if (print_x, print_y) in lights:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def render_lights(tick: int):
    background_colour = (0, 0, 0)           # Black.
    off_colour = (40, 40, 40)               # Grey
    on_colour = (255, 255, 255)

    screen.fill(background_colour)

    for render_y in range(grid_y):
        for render_x in range(grid_x):
            if (render_x, render_y) in lights:
                bulb = on_colour
            else:
                bulb = off_colour
            pygame.draw.circle(screen, color=bulb,
                               center=(scale + render_x * scale, scale + render_y * scale), radius=2)

    screenshot_name = 'screenshots/screen' + format(tick, '03') + '.png'
    pygame.image.save(screen, screenshot_name)
    filenames.append(screenshot_name)
    pygame.display.flip()


grid_x, grid_y = 0, 0
for row in t.split('\n'):
    grid_x = 0
    for position in row:
        if position == '#':
            lights.add((grid_x, grid_y))
        grid_x += 1
    grid_y += 1

always_on = set()

# Required for Part 2.
always_on.add((0, 0))
always_on.add((0, grid_y - 1))
always_on.add((grid_x - 1, 0))
always_on.add((grid_x - 1, grid_y - 1))
print(always_on)

lights = lights.union(always_on)

pygame.init()                                               # Initialize the game engine.

screen_size = [scale * (grid_x + 1), scale * (grid_y + 1)]  # [width, height]
screen = pygame.display.set_mode(screen_size)

print_lights()
render_lights(tick=0)

for generation in range(100):
    new_lights = always_on.copy()

    for x in range(grid_x):
        for y in range(grid_y):
            if (x, y) not in always_on:
                # Count neighbors.
                neighbors = 0
                for dx, dy in [(-1, -1), (0, -1), (1, -1),
                               (-1, 0),           (1, 0),
                               (-1, 1), (0, 1),   (1, 1)]:
                    if (x + dx, y + dy) in lights:
                        neighbors += 1

                # print(x, y, neighbors)

                if (x, y) in lights and neighbors in [2, 3]:
                    new_lights.add((x, y))
                elif (x, y) not in lights and neighbors == 3:
                    new_lights.add((x, y))

    lights = new_lights.copy()
    print_lights()
    render_lights(tick=generation + 1)

pygame.quit()

print(len(lights))
