def part_one():
    with open("input/1.txt") as f:
        parenthesis = f.readlines()[0]


    floor = 0
    for par in parenthesis:
        if par == "(":
            floor += 1
        else:
            floor -= 1

    return floor

def part_two():
    with open("input/1.txt") as f:
        parenthesis = f.readlines()[0]

    floor = 0
    for idx,par in enumerate(parenthesis):
        if par == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return idx +1

print(part_two())