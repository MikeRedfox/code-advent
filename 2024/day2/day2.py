import numpy as np


def is_ordered(data) -> bool:
    if (np.sort(data) != data).any() and (np.sort(data)[::-1] != data).any():
        return False
    return True


def is_report_safe(data) -> bool:
    for i in range(1,len(data)):
        # print(np.abs(data[i] - data[i-1]))
        if np.abs(data[i] - data[i-1]) > 3:
            return False
        if data[i] == data[i-1]:
            return False

    if not is_ordered(data):
        return False
    return True

def number_of_infractions(data) ->int:
    dngLvl = 0
    for i in range(1,len(data)):
        # print(np.abs(data[i] - data[i-1]))
        if np.abs(data[i] - data[i-1]) > 3:
            dngLvl += 1
        if data[i] == data[i-1]:
            dngLvl += 1
    if not is_ordered(data):
        dngLvl +=1
    return dngLvl


def part_one():
    with open("/home/mike/scripts/code-advent/2024/input/day2.txt") as f:
        data = f.readlines()
        data = [i.replace("\n","").split(' ') for i in data]
        data_ref = []
        for i in data:
            temp = []
            for j in i:
                temp.append(int(j))
            data_ref.append(temp)
    # print(data_ref)
    counter = 0
    for report in data_ref:
        if is_report_safe(report):
            counter += 1
    print(counter)
    return counter


def part_two():

    # with open("/home/mike/scripts/code-advent/2024/input/day2.example") as f:
    with open("/home/mike/scripts/code-advent/2024/input/day2.txt") as f:
        data = f.readlines()
        data = [i.replace("\n","").split(' ') for i in data]
        data_ref = []
        for i in data:
            temp = []
            for j in i:
                temp.append(int(j))
            data_ref.append(temp)
    co = 0
    for i in data_ref:
        is_safe_rem = 0
        if is_report_safe(i):
            co += 1
            print("Safe without removing")
            continue
        for j in i:
            tmp = i.copy()
            tmp.remove(j)

            if is_report_safe(tmp):
                is_safe_rem += 1

        print(f'Removing {is_safe_rem} levels makes it OK')
        if is_safe_rem != 0:
            co += 1
    print("-"*8)
    print(co)
    return co

print("-"*8)
part_two()
