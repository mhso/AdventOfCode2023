def part_1(input_lines):
    times = list(map(int, input_lines[0].split(None)[1:]))
    distances = list(map(int, input_lines[1].split(None)[1:]))

    result = 1
    for max_time, max_dist in zip(times, distances):
        speed = 0
        solutions = 0
        for time_left in range(max_time, -1, -1):
            if speed * time_left > max_dist:
                solutions += 1

            speed += 1

        result *= solutions

    print(result)


def part_2(input_lines):
    time = int("".join(input_lines[0].split(None)[1:]))
    distance = int("".join(input_lines[1].split(None)[1:]))

    speed = 0
    solutions = 0
    for time_left in range(time, -1, -1):
        if speed * time_left > distance:
            solutions += 1

        speed += 1

    print(solutions)
