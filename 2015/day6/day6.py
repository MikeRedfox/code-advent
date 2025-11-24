import numpy as np


def getIndexes(s):
    a, b = s.split(",")
    a = int(a)
    b = int(b)
    return a, b


def accendi(m, i, j, k, l):
    m[i : k + 1, j : l + 1] += 1
    return m


def spegni(m, i, j, k, l):
    # m[i : k + 1, j : l + 1] = m[i : k + 1, j : l + 1] -1 if m[i : k + 1, j : l + 1] > 0 else 0
    for tempI in range(i, k+1):
            for tempJ in range(j, l+1):
                if m[tempI][tempJ] > 0:
                        m[tempI][tempJ] -= 1

    return m


def toggle(m, i, j, k, l):
    m[i : k + 1, j : l + 1] += 2

    # for tempI in range(i, k+1):
    #     for tempJ in range(j, l+1):
    #         if m[tempI][tempJ] == 0:
    #             m[tempI][tempJ] = 1
    #         elif m[tempI][tempJ] == 1:
    #             m[tempI][tempJ] = 0
    return m


def part1():
    with open("../input/6.txt", "r") as f:
        inst = f.readlines()
    inst = [i.replace("\n", "").split(" ") for i in inst]
    mat = np.zeros([1000, 1000])
    for instruction in inst:
        command = instruction[0]
        i, j = getIndexes(instruction[1])
        k, l = getIndexes(instruction[3])
        if command == "a":
            mat = accendi(mat, i, j, k, l)
        elif command == "s":
            mat = spegni(mat, i, j, k, l)
        elif command == "t":
            mat = toggle(mat, i, j, k, l)

    print(np.sum(mat))


part1()
# m = np.zeros([3,3])
# print(toggle(m,0,0,2,2))
