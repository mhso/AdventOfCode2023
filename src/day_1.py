def part_1(input_lines):
    result = 0
    for line in input_lines:
        first = None
        prev_match = None
        for c in line:
            if 48 <= ord(c) <= 57:
                if prev_match is None:
                    first = c

                prev_match = c

        result += int(first + prev_match)

    print(result)


def part_2(input_lines):
    result = 0
    keywords = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    def parse_val(v):
        try:
            return str(int(v))
        except ValueError:
            return str(keywords.index(v) + 1)

    for line in input_lines:
        first = None
        best_match_first = len(line)
        last = None
        best_match_last = len(line)

        for keyword in keywords:
            index_first = line.find(keyword)
            if -1 < index_first < best_match_first:
                first = keyword
                best_match_first = index_first

            index_last = "".join(reversed(line)).find("".join(reversed(keyword)))

            if -1 < index_last < best_match_last:
                last = keyword
                best_match_last = index_last

        if last is None:
            last = first

        result += int(parse_val(first) + parse_val(last))

    print(result)
