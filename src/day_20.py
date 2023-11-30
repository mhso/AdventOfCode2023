def part_1(input_text):
    numbers = [int(num) for num in input_text]
    original_numbers = list(numbers)
    for index in range(len(numbers)):
        new_index = index + original_numbers[index]

        if new_index >= len(numbers):
            new_index = len(numbers) - new_index
        elif new_index < 0:
            new_index = len(numbers) - (index + numbers[index])

        numbers.pop(index)
        numbers.insert(new_index, original_numbers[index])
        print(numbers)

    print(numbers)

def part_2(input_text):
    print(input_text)
