import numpy as np


def get_binary_matrix(lines):
    binary_matrix = np.zeros((len(lines), len(lines[0].strip())))
    sum_galaxy = 0
    galaxy_positions = []
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line):
            if char == "#":
                sum_galaxy += 1
                galaxy_positions.append((i, j))
                binary_matrix[i][j] = sum_galaxy
    return binary_matrix, galaxy_positions


def get_empty_lines_columns(binary_matrix):
    empty_columns = []
    empty_lines = []
    for i in range(binary_matrix.shape[0]):
        if binary_matrix[i].sum() == 0:
            empty_lines.append(i)
    for i in range(binary_matrix.shape[1]):
        if binary_matrix[:, i].sum() == 0:
            empty_columns.append(i)
    return empty_lines, empty_columns


def get_new_binary_matrix(binary_matrix, empty_lines, empty_columns):
    for i, el in enumerate(empty_lines):
        binary_matrix = np.insert(
            binary_matrix, el + i, np.zeros(binary_matrix.shape[1]), 0
        )
    for i, el in enumerate(empty_columns):
        binary_matrix = np.insert(
            binary_matrix, el + i, np.zeros(binary_matrix.shape[0]), 1
        )
    new_galaxy_positions = []
    for i in range(binary_matrix.shape[0]):
        for j in range(binary_matrix.shape[1]):
            if binary_matrix[i][j] != 0:
                new_galaxy_positions.append((i, j))
    return binary_matrix, new_galaxy_positions


def part1(galaxy_positions):
    lengths = 0
    for i, galaxy1 in enumerate(galaxy_positions):
        for j, galaxy2 in enumerate(galaxy_positions[i:]):
            lengths += np.abs(galaxy2[0] - galaxy1[0]) + np.abs(galaxy2[1] - galaxy1[1])
    return lengths


def part2(galaxy_positions, empty_lines, empty_columns):
    lengths = 0
    for i, galaxy1 in enumerate(galaxy_positions):
        for j, galaxy2 in enumerate(galaxy_positions[i:]):
            col_span = 0
            line_span = 0
            for lin in empty_lines:
                if (galaxy2[0] < lin < galaxy1[0]) or (galaxy1[0] < lin < galaxy2[0]):
                    line_span += 1000000 - 1
            for col in empty_columns:
                if (galaxy2[1] < col < galaxy1[1]) or (galaxy1[1] < col < galaxy2[1]):
                    col_span += 1000000 - 1
            lengths += (
                np.abs(galaxy2[0] - galaxy1[0])
                + np.abs(galaxy2[1] - galaxy1[1])
                + line_span
                + col_span
            )
    return lengths


if __name__ == "__main__":
    input = open("input_day11.txt", "r")
    lines = input.readlines()
    binary_matrix, galaxy_positions = get_binary_matrix(lines)
    empty_lines, empty_columns = get_empty_lines_columns(binary_matrix)
    binary_matrix, new_galaxy_positions = get_new_binary_matrix(
        binary_matrix, empty_lines, empty_columns
    )
    res1 = part1(new_galaxy_positions)

    res2 = part2(galaxy_positions, empty_lines, empty_columns)

    print(res1, res2)
