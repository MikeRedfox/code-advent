with open("input/2.txt", "r") as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]


# lines = ['A Y','B X','C Z']

d1 = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

d2 = {"X": 1, "Y": 2, "Z": 3}

d3 = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},
    "B": {"X": "X", "Y": "Y", "Z": "Z"},
    "C": {"X": "Y", "Y": "Z", "Z": "X"},
}


def part1():
    s = []
    for line in lines:
        avv, me = line[0], line[-1]
        ss = d1[avv][me] + d2[me]
        s.append(ss)

    return sum(s)


def part2():
    s = []
    for line in lines:
        avv, me = line[0], line[-1]
        ss = d1[avv][d3[avv][me]] + d2[d3[avv][me]]
        s.append(ss)

    return sum(s)

    return


if __name__ == "__main__":
    print(part1())
    print(part2())

