# Solution to part 1 of day 6 of AOC 2015, Probably a Fire Hazard.
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


def main():
    screen_size = [1000, 1000]  # [width, height]

    # Each member is a pair (x, y) meaning that light is on at that coordinate.
    on = set()

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
                if command == 'on':
                    on.add((x, y))
                elif command == 'off':
                    if (x, y) in on:
                        on.remove((x, y))
                else:                                                   # Must be toggle.
                    if (x, y) in on:
                        on.remove((x, y))
                    else:
                        on.add((x, y))

        if len(instructions) == 0:
            pygame.init()                                               # Initialize the game engine.
            screen = pygame.display.set_mode(screen_size)

            # Define the colors we will use in RGB format.
            on_colour = (255, 255, 255)
            off_colour = (0, 0, 0)

            screen.fill(off_colour)

            for x in range(screen_size[0]):
                for y in range(screen_size[1]):
                    if (x, y) in on:
                        screen.set_at((x, y), on_colour)

            pygame.display.flip()

            pygame.image.save(screen, 'screenshots/day6_1_final.jpg')

            print('Part 1:', len(on))

    pygame.quit()


if __name__ == "__main__":
    main()
