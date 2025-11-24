def part_one():
    with open("input/2.txt") as f:
        s = f.readlines()
    ss = []
    for stringa in s:
        ss.append(stringa.replace('\n',''))
    somma = 0
    for stringa in ss:
        a,b,c = stringa.split('x')
        a = int(a)
        b = int(b)
        c = int(c)
        somma += 2*a*b + 2*b*c + 2*a*c +min(a*b,b*c,a*c)

    return somma

def part_two():
    with open("input/2.txt") as f:
        s = f.readlines()
    ss = []
    for stringa in s:
        ss.append(stringa.replace('\n',''))
    somma = 0
    for stringa in ss:
        a,b,c = stringa.split('x')
        a = int(a)
        b = int(b)
        c = int(c)
        somma += a*b*c + min(2*(a+b),2*(b+c),2*(a+c))

    return somma

print(part_two())