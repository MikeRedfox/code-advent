import numpy as np

def part_one():
    with open('input/8.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)

    # steps = "LLR"*10
    # myd = {'AAA':['BBB','BBB'],
    #         'BBB':['AAA','ZZZ'],
    #         'ZZZ':['ZZZ','ZZZ']}

    steps = ss[0] * 100
    myd = {}
    for idx,val in enumerate(ss):
        if idx == 0 or idx == 1:
            continue
        else:
            sx, dx = val.split('=')
            sx = sx[:-1]
            left = dx.split(',')[0][2:]
            right = dx.split(',')[1][1:-1]
            myd.update({sx:[left,right]})

    i = 1
    key = 'AAA'
    for direction in steps:
        if direction == 'R':
            idx = 1
        else:
            idx = 0
        
        key = myd[key][idx]
        if key == 'ZZZ':
            return i
        i += 1

    return 

def part_two():

    with open('input/8.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


#     steps = 'LR'*10
#     myd = {
# '11A' : ('11B', 'XXX'),
# '11B' : ('XXX', '11Z'),
# '11Z' : ('11B', 'XXX'),
# '22A' : ('22B', 'XXX'),
# '22B' : ('22C', '22C'),
# '22C' : ('22Z', '22Z'),
# '22Z' : ('22B', '22B'),
# 'XXX' : ('XXX', 'XXX')}
    steps = ss[0] * 1000
    myd = {}
    for idx,val in enumerate(ss):
        if idx == 0 or idx == 1:
            continue
        else:
            sx, dx = val.split('=')
            sx = sx[:-1]
            left = dx.split(',')[0][2:]
            right = dx.split(',')[1][1:-1]
            myd.update({sx:[left,right]})



    keys = [i for i in myd.keys() if i[-1]=='A']
    i = 1
    sol = []
    for direction in steps:
        if direction == 'R':
            idx = 1
        else:
            idx = 0
        new_keys = []
        for key in keys:
            new_keys.append(myd[key][idx])
            if myd[key][idx][-1] == 'Z':
                sol.append(i)
        
        if len(sol) == 6:
            break
        
        i += 1
        keys = new_keys

    
    for i in range(5):
        fin = np.lcm(sol[i],sol[i+1])        
    return fin


print(part_two())

