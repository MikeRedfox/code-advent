from utils import get_data


def part1():
    ranges = []
    ids = []
    for i in data:
        if "-" in i:
            ranges.append(i)
        else:
            ids.append(i)

    ids = [int(i) for i in ids if i != ""]
    added_ids = []
    fresh_ingredients = 0
    # print(ranges,ids)
    for id in ids:
        for rngs in ranges:
            l, r = rngs.split("-")
            l = int(l)
            r = int(r)
            # print(l,r,id, id in range(l,r+1))
            if id in range(l,r+1) and id not in added_ids:
                fresh_ingredients += 1
                added_ids.append(id)
    return fresh_ingredients

def part2():
    ranges = []

    for i in data:
        if "-" in i:
            ranges.append(i)

    intervals = []
    for r in ranges:
        l, u = r.split("-")
        intervals.append((int(l), int(u)))

    intervals = sorted(intervals, key=lambda interval: interval[0])
    refined = []
    current = intervals[0]
    for i in intervals[1:]:
        l,r = i
        if l <= current[1] + 1:
            current = (current[0], max(current[1],r))
        else:
            refined.append(current)
            current = (l, r)
    s = 0
    refined.append(current)
    for i in refined:
        s += (i[1]-i[0] + 1)
    print(s)




data = get_data("./inputs/5.txt")
print(part2())
