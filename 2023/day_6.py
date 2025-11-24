
def part_one():
    time = [61, 70, 90, 66]
    distance = [643, 1184, 1362, 1041]
    ns = 1

    for i in range(len(time)):
        n = 0
        for v in range(1,time[i]):
            d = v * (time[i] - v)
            # print(f'Hold down for {v} milliseconds: Travel for {d} millimeters')
            if d > distance[i]:
                n += 1
        ns *= n


    return ns

def part_two():
    
    time = [61, 70, 90, 66]
    distance = [643, 1184, 1362, 1041]
    time = int("".join([str(i) for i in time]))
    distance = int("".join([str(i) for i in distance]))

    n = 0

    for v in range(1,time):
        d = v * (time - v)
        if d > distance:
            n += 1
    

    return n



print(part_two())

