import numpy as np
def part_one():
    with open('input/11.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


    ss = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

    c = 1
    ss = np.array([i for i in ss if i != '\n']).reshape([10,10])
    for i in range(ss.shape[0]):
        for j in range(ss.shape[1]):
            if ss[i][j] == '#':
                ss[i][j] = c
                c += 1
            else:
                ss[i][j] = 0

    ss = [[j for j in i] for i in ss]
    for idx,row in enumerate(ss):
        somma_row = sum([int(i) for i in row])
        if somma_row == 0:
            ss[idx] = ss[idx] * 2

    
    print(ss)

    return

def part_two():

    with open('input/11.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


    return



print(part_one())

