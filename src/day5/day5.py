import re


def part1(lines):
    converted_seeds = []
    seeds = []
    for line in lines:
        line = line.strip()
        if line != "":
            if line.startswith("seeds"):
                converted_seeds = line.split(": ")[-1].split(" ")
                converted_seeds = [int(seed) for seed in converted_seeds]
            elif ":" in line:
                seeds = converted_seeds.copy()
                converted_seeds = []
            else:
                [destination_start, source_start, range_length] = line.split(" ")
                for seed in seeds:
                    if (
                        int(source_start)
                        <= seed
                        <= (int(source_start) + int(range_length))
                    ):
                        converted_seeds.append(
                            int(destination_start) + (seed - int(source_start))
                        )
    return min(converted_seeds)


def part2(lines):
    converted_seeds = []
    seeds = []
    for line in lines:
        line = line.strip()
        if line != "":
            if line.startswith("seeds"):
                converted_seeds_raw = line.split(": ")[-1].split(" ")
                converted_seeds = []
                for i in range(len(converted_seeds_raw)):
                    if i % 2 == 0:
                        converted_seeds.append(
                            (
                                int(converted_seeds_raw[i]),
                                int(converted_seeds_raw[i + 1]),
                            )
                        )
                    else:
                        pass
            elif ":" in line:
                seeds = converted_seeds.copy()
                converted_seeds = []
            else:
                [destination_start, source_start, range_length] = line.split(" ")
                for seed in seeds:
                    if (
                        int(source_start)
                        <= seed[0]
                        <= (int(source_start) + int(range_length))
                    ):
                        if (
                            int(source_start)
                            <= seed[0] + seed[1]
                            <= (int(source_start) + int(range_length))
                        ):
                            converted_seeds.append(
                                (
                                    int(destination_start)
                                    + (seed[0] - int(source_start)),
                                    seed[1],
                                )
                            )
                        else:
                            converted_seeds.append(
                                (
                                    int(destination_start)
                                    + (seed[0] - int(source_start)),
                                    int(range_length),
                                )
                            )
                            seeds.append(
                                (
                                    int(source_start) + int(range_length) + 1,
                                    seed[0] + seed[1],
                                )
                            )
                        seeds.remove(seed)
                    elif (
                        int(source_start)
                        <= seed[1]
                        <= (int(source_start) + int(range_length))
                    ):
                        converted_seeds.append(
                            (int(destination_start), seed[1] - int(source_start))
                        )
                        seeds.append((seed[0], int(source_start) - seed[0]))
                        seeds.remove(seed)
                    else:
                        pass
    min_seed = float("inf")
    for seed in converted_seeds:
        if min_seed > seed[0]:
            min_seed = seed[0]
    return min_seed


if __name__ == "__main__":
    input = open("input_day5.txt", "r")
    lines = input.readlines()
    res1 = part1(lines)

    res2 = part2(lines)

    print(res1, res2)
