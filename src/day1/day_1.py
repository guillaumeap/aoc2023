import regex as reg


def part1(lines):
    int_sum = 0
    for line in lines:
        first_int = None
        last_int = None
        new_line = line.strip()
        for char in new_line:
            try:
                u = int(char)
                if first_int is None:
                    first_int = u
                last_int = u
            except ValueError:
                continue
        int_sum += int(str(first_int) + str(last_int))
    return int_sum


def part2(lines):
    conv_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    int_sum = 0
    for line in lines:
        new_line = line.strip()
        all_matches = reg.findall(
            r"\d{1}|one|two|three|four|five|six|seven|eight|nine",
            new_line,
            overlapped=True,
        )
        first_match = all_matches[0]
        last_match = all_matches[-1]
        if first_match in conv_dict:
            first_match = conv_dict[first_match]
        if last_match in conv_dict:
            last_match = conv_dict[last_match]
        to_add = int(str(first_match) + str(last_match))
        int_sum += to_add
    return int_sum


if __name__ == "__main__":
    input = open("input_1_day_1.txt", "r")
    lines = input.readlines()
    res1 = part1(lines)

    input = open("input_1_day_1.txt", "r")
    lines = input.readlines()
    res2 = part2(lines)

    print(res1, res2)
