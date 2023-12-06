import numpy as np


def get_time_distance(lines):
    times = lines[0].strip().split(":        ")[-1].split("     ")
    times = [int(el) for el in times]
    distances = lines[1].strip().split(":   ")[-1].split("   ")
    distances = [int(el) for el in distances]
    return times, distances


def part1(times, distances):
    print(times, distances)
    list_success = []
    for j, time in enumerate(times):
        time_success = 0
        for i in range(time):
            if i * (time - i) > distances[j]:
                time_success += 1
        list_success.append(time_success)
    return np.product(list_success)


if __name__ == "__main__":
    input = open("input_day6.txt", "r")
    lines = input.readlines()

    times, distances = get_time_distance(lines)

    res1 = part1(times, distances)

    new_times, new_distances = [int("".join([str(el) for el in times]))], [
        int("".join([str(el) for el in distances]))
    ]

    res2 = part1(new_times, new_distances)

    print(res1, res2)
