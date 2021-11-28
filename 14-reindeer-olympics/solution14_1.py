# Solution to part 1 of day 14 of AOC 2015, Reindeer Olympics
# https://adventofcode.com/2015/day/14

f = open('test.txt')
whole_text = f.read()
f.close()

race = 2503
best = 0

for line in whole_text.split('\n'):
    print(line)

    # Example,
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    reindeer, _, _, speed_str, _, _, fly_str, _, _, _, _, _, _, rest_str, _ = line.split(' ')
    speed, fly, rest = int(speed_str), int(fly_str), int(rest_str)

    complete_fly_rest_cycles = race // (fly + rest)

    final_flight_start_second = complete_fly_rest_cycles * (fly + rest)
    time_left_for_final_flight = race - final_flight_start_second
    final_flight_secs = min(fly, time_left_for_final_flight)

    fly_time = complete_fly_rest_cycles * fly + final_flight_secs

    dist = fly_time * speed
    best = max(best, dist)

    print('reindeer:', reindeer)
    print('speed:', speed)
    print('fly:', fly)
    print('rest:', rest)
    print('complete_fly_rest_cycles:', complete_fly_rest_cycles)
    print('final_flight_start_second:', final_flight_start_second)
    print('time_left_for_final_flight', time_left_for_final_flight)
    print('final_flight_secs', final_flight_secs)
    print('fly_time:', fly_time)
    print('dist:', dist)
    print()

print(best)
