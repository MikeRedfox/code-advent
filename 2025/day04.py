from utils import get_data

# print(data)

def get_neighbours(m:list[str],i: int,j: int):
    s = 0
    for k in range(-1, 2):
        for y in range(-1, 2):
            if i+k >= 0 and i+k < len(m) and j+y >= 0 and j+y < len(m) and (k!=0 or y != 0):
                # print(i+k,j+y, len(m))
                if m[i+k][j+y] == "@":
                    s += 1
    return s

def part1():
    res = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if get_neighbours(data,i,j) < 4 and data[i][j] == "@":
                res += 1

    return res

def part2():
    running = True
    s = 0
    while running:
        res = 0
        for i in range(len(data)):
            for j in range(len(data)):
                if get_neighbours(data,i,j) < 4 and data[i][j] == "@":
                    old = data[i]
                    new = old[0:j] + "." + old[j+1:]
                    data[i] = new
                    res += 1
        s += res
        if res == 0:
            running = False
    return s




data = get_data("./inputs/4.txt")
print(part2())

