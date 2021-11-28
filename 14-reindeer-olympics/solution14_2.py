# Solution to part 2 of day 14 of AOC 2015, Reindeer Olympics
# https://adventofcode.com/2015/day/14

f = open('input.txt')
whole_text = f.read()
f.close()

race = 2503
deers = {}
all_deers = {}

for line in whole_text.split('\n'):
    # print(line)

    # Example,
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    reindeer, _, _, speed_str, _, _, fly_str, _, _, _, _, _, _, rest_str, _ = line.split(' ')
    speed, fly, rest = int(speed_str), int(fly_str), int(rest_str)

    deers[reindeer] = 0

    for second in range(1, race + 1):
        # print(second)

        complete_fly_rest_cycles = second // (fly + rest)

        final_flight_start_second = complete_fly_rest_cycles * (fly + rest)
        time_left_for_final_flight = second - final_flight_start_second
        final_flight_secs = min(fly, time_left_for_final_flight)

        fly_time = complete_fly_rest_cycles * fly + final_flight_secs

        dist = fly_time * speed

        all_deers[(reindeer, second)] = dist

for second in range(1, race + 1):
    best_dist_this_sec = 0
    best_deers_this_sec = []

    for deer in deers:
        if all_deers[(deer, second)] > best_dist_this_sec:
            best_dist_this_sec = all_deers[(deer, second)]
            best_deers_this_sec = [deer]
        elif all_deers[(deer, second)] == best_dist_this_sec:
            best_deers_this_sec.append(deer)

    for deer in best_deers_this_sec:
        deers[deer] += 1

print()
print(deers)
