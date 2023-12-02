def part_1(input_lines):
    result = 0

    for line in input_lines:
        color_counts = {"red": 0, "green": 0, "blue": 0}
        split_1 = line.split(":")
        game_index = int(split_1[0].split(" ")[1])
        split_2 = split_1[1].strip().split(";")
        for round in split_2:
            cubes = round.strip().split(",")
            for cube in cubes:
                count, color = cube.strip().split(" ")
                color_counts[color] = max(color_counts[color], int(count))

        if color_counts["red"] <= 12 and color_counts["green"] <= 13 and color_counts["blue"] <= 14:
            result += game_index

    print(result)

def part_2(input_lines):
    result = 0

    for line in input_lines:
        color_counts = {"red": 0, "green": 0, "blue": 0}
        split_1 = line.split(":")
        split_2 = split_1[1].strip().split(";")
        for round in split_2:
            cubes = round.strip().split(",")
            for cube in cubes:
                count, color = cube.strip().split(" ")
                color_counts[color] = max(color_counts[color], int(count))

        result += color_counts["red"] * color_counts["green"] * color_counts["blue"]

    print(result)
