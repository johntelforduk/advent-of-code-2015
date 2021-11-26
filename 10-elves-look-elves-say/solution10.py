# Solution to day 10 of AOC 2015, Elves Look, Elves Say
# https://adventofcode.com/2015/day/10

new_sequence = '1113222113'

for i in range(50):
    print('i, len(new_sequence)', i, len(new_sequence))

    sequence = new_sequence
    run_digit = None
    run_length = 0
    new_sequence = ''

    for head in sequence:
        if run_digit is not None and run_digit != head:                 # Time to add to new_sequence.
            new_sequence = new_sequence + str(run_length) + run_digit

            # Start new run.
            run_length = 1
        else:
            run_length += 1

        run_digit = head
    new_sequence = new_sequence + str(run_length) + run_digit           # Time to add to new_sequence.
#    print('sequence, new_sequence:', new_sequence)

print('Solution:', len(new_sequence))
