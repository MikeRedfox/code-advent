import numpy as np

# NOTE: First tried this day 😃

def part_one():
    lines = np.loadtxt("../input/day1.txt")
    first = lines[:,0]
    second = lines[:,1]
    first.sort()
    second.sort()
    diff = np.abs(first - second)

    print(diff.sum())
    return diff.sum()


def part_two():
    lines = np.loadtxt("../input/day1.txt")
    first = lines[:,0]
    second = lines[:,1]
    s = 0
    for i in first:
        i_appearance = 0
        for j in second:
            if i == j:
                i_appearance += 1
        s += (i*i_appearance)
    print(s)
    return(s)

# part_one()
part_two()
