def hash_sequence(s:str):

    temp = 0
    for i in s:
        temp += ord(i)
        temp *= 17
        temp = temp % 256
    
    return temp


def part_one():
    # ss = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    from input_15 import ss
    solution = sum([hash_sequence(i) for i in ss.split(',')])

    return solution

def part_two():

    with open('input/15.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


    return



print(part_one())

