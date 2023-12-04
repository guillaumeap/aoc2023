import re


def part1(lines):
    global_sum = 0
    for line in lines:
        line = line.split("\n")[0]
        winning_numbers = re.findall("[0-9]+", line.split(":")[-1].split("|")[0])
        my_numbers = re.findall("[0-9]+", line.split(":")[-1].split("|")[-1])
        matches = 0
        for number in winning_numbers:
            if number in my_numbers:
                matches += 1
        if matches > 0:
            global_sum += 2 ** (matches - 1)
    return global_sum


def part2(lines):
    original_dict = {k: 1 for k in range(1, len(lines) + 1)}
    for i, line in enumerate(lines):
        line = line.split("\n")[0]
        winning_numbers = re.findall("[0-9]+", line.split(":")[-1].split("|")[0])
        my_numbers = re.findall("[0-9]+", line.split(":")[-1].split("|")[-1])
        matches = 0
        for number in winning_numbers:
            if number in my_numbers:
                matches += 1
        for match in range(matches):
            original_dict[i + match + 2] += original_dict[i + 1]
    return sum(original_dict.values())


if __name__ == "__main__":
    input = open("input_day4.txt", "r")
    lines = input.readlines()
    res1 = part1(lines)

    res2 = part2(lines)

    print(res1, res2)
