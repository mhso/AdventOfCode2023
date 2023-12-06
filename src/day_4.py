def part_1(input_lines):
    result = 0

    for line in input_lines:
        split_1 = line.split("|")
        split_2 = split_1[0].strip().split(":")
        split_3 = set(map(int, split_2[1].strip().split(None)))
        split_4 = set(map(int, split_1[1].strip().split(None)))

        winning_nums = split_3.intersection(split_4)

        if winning_nums:
            result += 2 ** (len(winning_nums) - 1)

    print(result)


def part_2(input_lines):
    winning_card_nums = []
    pending_cards = []

    for card_num, line in enumerate(input_lines):
        split_1 = line.split("|")
        split_2 = split_1[0].strip().split(":")
        winning_nums = set(split_2[1].strip().split(None)).intersection(
            set(split_1[1].strip().split(None))
        )

        pending_cards.append(card_num)
        winning_card_nums.append(len(winning_nums))

    result = len(pending_cards)
    while pending_cards != []:
        card = pending_cards.pop()
        pending_cards.extend(range(card + 1, card + winning_card_nums[card] + 1))
        result += winning_card_nums[card]

    print(result)
