with open('input/1.txt','r') as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]

# lines = ['1','2','3','','4','','5','6','','7','8','9','','10']


def part1():

    l = []
    i = 0
    current = []

    while i < len(lines):
        if lines[i] == '':
            l.append(current)
            current = []
            i += 1
        else:
            current.append(int(lines[i]))
            i += 1


    return max([sum(arr) for arr in l])


def part2():

    l = []
    i = 0
    current = []

    while i < len(lines):
        if lines[i] == '':
            l.append(current)
            current = []
            i += 1
        else:
            current.append(int(lines[i]))
            i += 1

    l = [sum(arr) for arr in l]

    def Nmaxelements(list1, N):
        final_list = []
    
        for i in range(0, N):
            max1 = 0
            
            for j in range(len(list1)):    
                if list1[j] > max1:
                    max1 = list1[j];
                    
            list1.remove(max1);
            final_list.append(max1)
        return final_list

    return sum(Nmaxelements(l, 3))


if __name__ == '__main__':
    print(part1())
    print(part2())
