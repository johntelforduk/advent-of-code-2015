# Solution to part 2 of day 6 of AOC 2015, Probably a Fire Hazard.
# https://adventofcode.com/2015/day/6

import pygame


def str_pair_to_ints(str_pair: str) -> (int, int):
    """For parm string like '61,44' return pair of ints like (61, 44)."""
    s1, s2 = str_pair.split(',')
    return int(s1), int(s2)


def parse_instruction(instruction: str) -> (str, int, int, int, int):
    """Parse the parm instruction. Return a tuple, (command, x1, y1, x2, y2)."""

    if 'turn on' in instruction:
        command = 'on'
        instruction = instruction.replace('turn on ', '')
    elif 'turn off' in instruction:
        command = 'off'
        instruction = instruction.replace('turn off ', '')
    else:
        command = 'toggle'
        instruction = instruction.replace('toggle ', '')

    [one, _, two] = instruction.split(' ')
    x1, y1 = str_pair_to_ints(one)
    x2, y2 = str_pair_to_ints(two)

    return command, x1, y1, x2, y2


def normalised_colour(brightness: int, maximum: int) -> (int, int, int):
    """For the parm brightness, return a tuple that is the normalised colour for that brightness."""

    intensity = brightness * 255 // maximum
    return intensity, intensity, intensity


def main():
    screen_size = [1000, 1000]  # [width, height]

    # Each member is a k: v. Where,
    # k = pair (x, y), the coordinates of the light.
    # v = brightness of the light.
    light = {}

    # Initialise all of the lights to zero brightness.
    for x in range(screen_size[0]):
        for y in range(screen_size[1]):
            light[(x, y)] = 0
    max_bright = 0

    f = open('input.txt')
    whole_text = f.read()
    f.close()

    instructions = whole_text.split('\n')

    while len(instructions) != 0:
        instruction = instructions.pop(0)
        command, x1, y1, x2, y2 = parse_instruction(instruction)
        print(instruction, command)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):

                # "The phrase turn on actually means that you should increase the brightness of those lights by 1."
                if command == 'on':
                    light[(x, y)] += 1
                    if light[(x, y)] > max_bright:
                        max_bright = light[(x, y)]

                # "The phrase turn off actually means that you should decrease the brightness of those lights by 1, to
                # a minimum of zero."
                elif command == 'off':
                    if light[(x, y)] > 0:
                        light[(x, y)] -= 1

                # Must be toggle.
                # "The phrase toggle actually means that you should increase the brightness of those lights by 2."

                else:
                    light[(x, y)] += 2
                    if light[(x, y)] > max_bright:
                        max_bright = light[(x, y)]

        if len(instructions) == 0:
            pygame.init()                                               # Initialize the game engine.
            screen = pygame.display.set_mode(screen_size)

            total_brightness = 0

            for x in range(screen_size[0]):
                for y in range(screen_size[1]):
                    total_brightness += light[(x, y)]

                    screen.set_at((x, y), normalised_colour(light[(x, y)], max_bright))

            pygame.display.flip()

            pygame.image.save(screen, 'screenshots/day6_2_final.jpg')

            print('Part 2:', total_brightness)

    pygame.quit()


if __name__ == "__main__":
    main()
