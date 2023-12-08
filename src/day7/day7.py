import numpy as np

def_dict = {
    "five_of_a_kind": [5],
    "four_of_a_kind": [1, 4],
    "full_house": [2, 3],
    "three_of_a_kind": [1, 1, 3],
    "two_pair": [1, 2, 2],
    "one_pair": [1, 1, 1, 2],
    "high_card": [1, 1, 1, 1, 1],
}
def_value = {
    "five_of_a_kind": 6,
    "four_of_a_kind": 5,
    "full_house": 4,
    "three_of_a_kind": 3,
    "two_pair": 2,
    "one_pair": 1,
    "high_card": 0,
}
dtype = [
    ("def", int),
    ("first", int),
    ("second", int),
    ("third", int),
    ("fourth", int),
    ("fifth", int),
    ("score", int),
]


def part1(lines):
    res = []
    card_value = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    for line in lines:
        line = line.strip()
        hand_points = int(line.split(" ")[-1])
        hand_value = line.split(" ")[0]
        hand_dict = {}
        for char in hand_value:
            if char in hand_dict:
                hand_dict[char] += 1
            else:
                hand_dict[char] = 1
        for defi in def_dict:
            b = def_dict[defi]
            c = list(hand_dict.values())
            b.sort()
            c.sort()
            if b == c:
                res.append(
                    (
                        def_value[defi],
                        card_value[hand_value[0]],
                        card_value[hand_value[1]],
                        card_value[hand_value[2]],
                        card_value[hand_value[3]],
                        card_value[hand_value[4]],
                        hand_points,
                    )
                )
    res_array = np.array(res, dtype=dtype)
    res_sorted = np.sort(
        res_array, order=["def", "first", "second", "third", "fourth", "fifth"]
    )
    final_score = 0
    for i, el in enumerate(res_sorted):
        final_score += (i + 1) * el[6]
    return final_score


def part2(lines):
    res = []
    card_value = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 1,
        "Q": 11,
        "K": 12,
        "A": 13,
    }
    for line in lines:
        line = line.strip()
        hand_points = int(line.split(" ")[-1])
        hand_value = line.split(" ")[0]
        hand_dict = {}
        jacks = 0
        for char in hand_value:
            if char == "J":
                jacks += 1
            elif char in hand_dict:
                hand_dict[char] += 1
            else:
                hand_dict[char] = 1
        if jacks == 5:
            hand_dict["J"] = 5
        elif jacks != 0:
            max_i = np.max(list(hand_dict.values()))
            for el in hand_dict:
                if hand_dict[el] == max_i:
                    hand_dict[el] += jacks
                    break
        for defi in def_dict:
            b = def_dict[defi]
            c = list(hand_dict.values())
            b.sort()
            c.sort()
            if b == c:
                res.append(
                    (
                        def_value[defi],
                        card_value[hand_value[0]],
                        card_value[hand_value[1]],
                        card_value[hand_value[2]],
                        card_value[hand_value[3]],
                        card_value[hand_value[4]],
                        hand_points,
                    )
                )
    res_array = np.array(res, dtype=dtype)
    res_sorted = np.sort(
        res_array, order=["def", "first", "second", "third", "fourth", "fifth"]
    )
    final_score = 0
    for i, el in enumerate(res_sorted):
        final_score += (i + 1) * el[6]
    return final_score


if __name__ == "__main__":
    input = open("input_day7.txt", "r")
    lines = input.readlines()
    res1 = part1(lines)
    res2 = part2(lines)

    print(res1, res2)
