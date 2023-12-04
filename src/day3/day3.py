import re


def count_number_and_symbols(lines):
    all_lines_number = [[]]
    all_lines_symbol = [[]]
    for line in lines:
        line = line.split("\n")[0]
        current_line_number = []
        current_line_symbol = []
        for number in re.finditer("[0-9]+", line):
            current_line_number.append((number.group(), number.start(), number.end()))
        for symbol in re.finditer("[^0-9]", line):
            if symbol.group() != ".":
                current_line_symbol.append((symbol.group(), symbol.start()))
        all_lines_number.append(current_line_number)
        all_lines_symbol.append(current_line_symbol)
    all_lines_number.append([])
    all_lines_symbol.append([])
    return all_lines_number, all_lines_symbol


def part1(all_lines_number, all_lines_symbol):
    total_count = 0
    for i, line in enumerate(all_lines_number):
        for number in line:
            counted = False
            for symbol_line in all_lines_symbol[i - 1 : i + 2]:
                for symbol in symbol_line:
                    if number[1] - 1 <= symbol[1] <= number[2]:
                        total_count += int(number[0])
                        counted = True
                    if counted:
                        break
                if counted:
                    break
    return total_count


def part2(all_lines_number, all_lines_symbol):
    total_count = 0
    for i, line in enumerate(all_lines_symbol):
        for symbol in line:
            if symbol[0] == "*":
                count = 0
                num = []
                for number_line in all_lines_number[i - 1 : i + 2]:
                    for number in number_line:
                        if number[1] - 1 <= symbol[1] <= number[2]:
                            count += 1
                            num.append(int(number[0]))
                        if count > 2:
                            break
                    if count > 2:
                        break
                if count == 2:
                    total_count += num[0] * num[1]
    return total_count


if __name__ == "__main__":
    input = open("input_day3.txt", "r")
    lines = input.readlines()

    all_lines_number, all_lines_symbol = count_number_and_symbols(lines)
    res1 = part1(all_lines_number, all_lines_symbol)

    res2 = part2(all_lines_number, all_lines_symbol)

    print(res1, res2)
