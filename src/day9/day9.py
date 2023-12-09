import numpy as np


def part1(lines):
    sum = 0
    for line in lines:
        last_digit = []
        line = line.strip()
        int_list = [int(el) for el in line.split(" ")]
        last_digit.append(int_list[-1])
        while (np.array(int_list) == 0).sum() != len(int_list):
            int_list = np.diff(int_list)
            last_digit.append(int_list[-1])
        sum += np.sum(last_digit)
    return sum


def part2(lines):
    sum = 0
    for line in lines:
        first_digit = []
        line = line.strip()
        int_list = [int(el) for el in line.split(" ")]
        first_digit.append(int_list[0])
        while (np.array(int_list) == 0).sum() != len(int_list):
            int_list = np.diff(int_list)
            first_digit.append(int_list[0])
        first_digit.reverse()
        new_digit = 0
        for dig in first_digit:
            new_digit = dig - new_digit
        sum += new_digit
    return sum


if __name__ == "__main__":
    input = open("input_day9.txt", "r")
    lines = input.readlines()
    res1 = part1(lines)

    res2 = part2(lines)

    print(res1, res2)
