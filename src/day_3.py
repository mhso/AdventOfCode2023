def symbol_adjacent(x, y, symbols):
    for a_x in range(x - 1, x + 2):
        for a_y in range(y - 1, y + 2):
            if (a_x, a_y) != (x, y) and (a_x, a_y) in symbols:
                return (a_x, a_y)
    
    return None

def part_1(input_lines):
    symbols = set()
    for y, line in enumerate(input_lines):
        for x, c in enumerate(line):
            if c == ".":
                continue

            try:
                int(c)
            except ValueError:
                symbols.add((x, y))

    result = 0

    for y, line in enumerate(input_lines):
        curr_number = ""
        number_valid = False
        for x, c in enumerate(line):
            try:
                int(c)
                curr_number += c
                if not number_valid and symbol_adjacent(x, y, symbols):
                    number_valid = True

            except ValueError:
                if number_valid and curr_number != "":
                    result += int(curr_number)

                curr_number = ""
                number_valid = False

        if number_valid and curr_number != "":
            result += int(curr_number)

    print(result)

def part_2(input_lines):
    gears = set()
    for y, line in enumerate(input_lines):
        for x, c in enumerate(line):
            if c == "*":
                gears.add((x, y))

    gear_counts = {}
    gear_nums = {}

    for y, line in enumerate(input_lines):
        curr_number = ""
        number_valid = False
        adjacent_gears = set()
        for x, c in enumerate(line):
            try:
                int(c)
                curr_number += c
                if not number_valid and (s_c := symbol_adjacent(x, y, gears)) is not None:
                    number_valid = True
                    adjacent_gears.add(s_c)

            except ValueError:
                if number_valid and curr_number != "":
                    for s_c in adjacent_gears:
                        gear_nums[s_c] = gear_nums.get(s_c, 1) * int(curr_number)
                        gear_counts[s_c] = gear_counts.get(s_c, 0) + 1

                curr_number = ""
                number_valid = False
                adjacent_gears = set()

        if number_valid and curr_number != "":
            for s_c in adjacent_gears:
                gear_nums[s_c] = gear_nums.get(s_c, 1) * int(curr_number)
                gear_counts[s_c] = gear_counts.get(s_c, 0) + 1

    result = 0
    for s_c in gear_counts:
        if gear_counts[s_c] == 2:
            result += gear_nums[s_c]

    print(result)
