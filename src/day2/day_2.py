def part1(lines):
    max_colors = {"red": 12, "green": 13, "blue": 14}
    game_sum = 0
    for line in lines:
        line = line.split("\n")[0]
        game_nb = line.split(": ")[0].split(" ")[-1]
        game_draws = line.split(": ")[-1].split("; ")
        to_count = True
        for draw in game_draws:
            color_draw = draw.split(", ")
            for color_nb in color_draw:
                color = color_nb.split(" ")[-1]
                nb = color_nb.split(" ")[0]
                if int(nb) > max_colors[color]:
                    to_count = False
        if to_count:
            game_sum += int(game_nb)
    return game_sum


def part2(lines):
    power_sum = 0
    for line in lines:
        line = line.split("\n")[0]
        game_nb = line.split(": ")[0].split(" ")[-1]
        game_draws = line.split(": ")[-1].split("; ")
        power_color = {"red": [0], "green": [0], "blue": [0]}
        power = 1
        for draw in game_draws:
            color_draw = draw.split(", ")
            for color_nb in color_draw:
                color = color_nb.split(" ")[-1]
                nb = color_nb.split(" ")[0]
                power_color[color].append(int(nb))
        for col in power_color:
            power *= max(power_color[col])
        power_sum += power
    return power_sum


if __name__ == "__main__":
    input = open("input_day_2.txt", "r")
    lines = input.readlines()
    res1 = part1(lines)

    input = open("input_day_2.txt", "r")
    lines = input.readlines()
    res2 = part2(lines)

    print(res1, res2)
