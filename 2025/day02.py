VVfrom utils import get_data

def part1(filepath: str):
    data = get_data(filepath)[0].split(",")
    s = 0
    for istruzione in data:
        l,r = istruzione.split("-")
        l = int(l)
        r = int(r)
        # print(l,r)
        for n in range(l,r+1):
            lun = len(str(n))
            nStr = str(n)
            # print(lun)
            half = lun // 2
            # print(nStr[0:half+1],nStr[half:])
            if lun % 2 == 0:
                half = lun // 2
                if nStr[0:half] == nStr[half:]:
                    # print(n)
                    s += n
    return s

def part2(filepath: str):
    data = get_data(filepath)[0].split(",")
    res: list[int] = []
    for istruzione in data:
        l,r = istruzione.split("-")
        l = int(l)
        r = int(r)
        for n in range(l,r+1):
            lun = len(str(n))
            nStr = str(n)
            half = lun // 2
            for j in range(2, half+1):
                for k in range(2,half+1):
                    if nStr[0:j]*k == nStr:
                        res.append(n)
            # nSorted = "".join(sorted(nStr))
            if (nStr[0:half] == nStr[half:]) or (len(set(nStr)) == 1 and len(nStr) != 1):
                res.append(n)
    # print(set(res))
    return sum(set(res))


print(part1("./inputs/2.txt"))
print(part2("./inputs/2.txt"))
