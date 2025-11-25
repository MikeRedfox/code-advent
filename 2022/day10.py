with open("./input/10.txt") as f:
    data = f.readlines()
    data = [i[:-1] for i in data]


def part1()-> int:
    d = {}
    i = 0
    x = 1
    for instruction in data:
        i += 1
        ins = instruction.split(" ")
        if len(ins) == 1:
            d[i] = x
        else:
            d[i] = x
            i += 1
            x+= int(ins[1])
            d[i] = x


    idx = [19,59,99,139,179,219]
    result:int = 0
    for i in idx:
        # print(d[i])
        result += d[i]*(i+1)
    return result


def part2():
    d = {}
    i = 0
    x = 1
    for instruction in data:
        i += 1
        ins = instruction.split(" ")
        if len(ins) == 1:
            d[i] = x
        else:
            d[i] = x
            i += 1
            x+= int(ins[1])
            d[i] = x


    d[0] = 1
    s = ""
    idx = 0
    for i in range(1,max(d.keys())+1):
        if (i-1) % 40 == 0:
            s += "\n"
            idx = 1
        # print(f"x = {d[i-1]}, index={idx}, {d[i-1] == idx or d[i-1] == idx+1 or d[i-1] == idx-1} ")
        if d[i-1] == idx or d[i-1] == idx-2 or d[i-1] == idx-1:
            s+= "#"
        else:
            s+="."
        idx +=1

    return s


print(part1())
print(part2())
