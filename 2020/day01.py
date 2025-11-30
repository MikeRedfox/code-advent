with open("./inputs/1.txt") as f:
    data = f.readlines()
    data = [int(i[:-1]) for i in data]

def part1():
    for i in data:
        for j in data:
            if i +j == 2020:
                return i*j

def part2():
    for i in data:
        for j in data:
            for k in data:
                if i +j +k == 2020:
                    return i*j*k

print(part2())
# print(data)
