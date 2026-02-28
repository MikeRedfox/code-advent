from utils import get_data
from math import prod

def get_column(m, i):
    c = []
    for row in m:
        r = row.split(" ")
        r = [j for j in r if j != ""]
        c.append(r[i])
    return c



def part1():
    s = 0
    for i in range(l):
        c = get_column(data, i)
        for j in range(len(c)-1):
            c[j] = int(c[j])
        if c[-1] == "+":
            s += sum(c[:-1])
        elif c[-1] == "*":
            s += prod(c[:-1])
    return s

# print(data[:][0:3])
# print(data[0:3])
# print(data)

def part2():
    global data

    d = []
    m2 = []

    zipped = list(zip(*data[:-1]))

    for c in zipped:
        col = "".join(c)
        d.append(col)
        try:
            m2.append(int(col))
        except:
            m2.append(None)  # placeholder neutro da sostituire più tardi

    l = len(data[:-1])
    m3 = [m2[i:i+l] for i in range(0, len(m2), l)]

    operazioni = [x for x in data[-1].split() if x != ""]

    # ⚡ Allinea il numero di gruppi con il numero di operazioni
    while len(m3) < len(operazioni):
        m3.append([None]*l)

    print(len(m3), len(operazioni))

    s = 0
    for i in range(len(operazioni)):
        gruppo = m3[i]
        if operazioni[i] == "+":
            gruppo = [0 if x is None else x for x in gruppo]
            s += sum(gruppo)
        elif operazioni[i] == "*":
            gruppo = [1 if x is None else x for x in gruppo]
            s += prod(gruppo)

    print(s)
    return s

data = get_data('./inputs/6.txt')
l = data[0].split(" ")
l = len([i for i in l if i != ''])

part2()


