with open("input/4.txt", "r") as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]


# lines = [
#     '2-4,6-8',
#    ' 2-3,4-5',
#     '5-7,7-9',
#     '2-8,3-7',
#     '6-6,4-6',
#     '2-6,4-8',
# ]


def prima_econtenutanella_seconda(l1, l2):

    for l in l1:
        if l not in l2:
            return False
    return True


def overlap(l1, l2):
    for l in l1:
        if l in l2:
            return True
    return False


def part1():

    s = []

    for line in lines:
        e1, e2 = line.split(",")
        a, b = e1.split("-")
        c, d = e2.split("-")
        l1 = list(range(int(a), int(b) + 1))
        l2 = list(range(int(c), int(d) + 1))

        if prima_econtenutanella_seconda(l1, l2) or prima_econtenutanella_seconda(
            l2, l1
        ):
            s.append(1)
    return sum(s)


def part2():

    s = []

    for line in lines:
        e1, e2 = line.split(",")
        a, b = e1.split("-")
        c, d = e2.split("-")
        l1 = list(range(int(a), int(b) + 1))
        l2 = list(range(int(c), int(d) + 1))

        if overlap(l1, l2):
            s.append(1)
    return sum(s)


if __name__ == "__main__":
    print(part1())
    print(part2())

