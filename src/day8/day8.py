import numpy as np


def get_connection_dict(lines):
    connection_dict = {}
    for line in lines[2:]:
        line = line.strip()
        connection_dict[line.split(" = (")[0]] = {}
        connection_dict[line.split(" = (")[0]]["L"] = line.split(" = (")[-1].split(
            ", "
        )[0]
        connection_dict[line.split(" = (")[0]]["R"] = (
            line.split(" = (")[-1].split(", ")[-1].split(")")[0]
        )
    return connection_dict


def part1(connection_dict, instruction):
    current = "AAA"
    step = 0
    while current != "ZZZ":
        current = connection_dict[current][instruction[step % len(instruction)]]
        step += 1
    return step


def part2(connection_dict, instruction):
    current_list = []
    for el in connection_dict:
        if el.endswith("A"):
            current_list.append(el)

    steps = []
    for current in current_list:
        step = 0
        while not current.endswith("Z"):
            current = connection_dict[current][instruction[step % len(instruction)]]
            step += 1
        steps.append(step)

    return np.lcm.reduce(steps)


if __name__ == "__main__":
    input = open("input_day8.txt", "r")
    lines = input.readlines()

    instruction = lines[0].strip()
    connection_dict = get_connection_dict(lines)

    res1 = part1(connection_dict, instruction)

    res2 = part2(connection_dict, instruction)

    print(res1, res2)
