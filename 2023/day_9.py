import numpy as np

def part_one():
    numbers = np.loadtxt('input/9.txt')
    somma = 0
    for line in numbers:
        
        diff = [line[i+1]-line[i] for i in range(line.size - 1)]
        value = diff[-1]
        while np.sum(diff) != 0:
            diff = [diff[i+1] - diff[i] for i in range(len(diff) - 1)]
            value += diff[-1]
        print(value + line[-1])
        somma += value + line[-1]

    return int(somma)

def part_two():

    with open('input/9.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


    return



print(part_one())

