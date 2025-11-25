with open("./input/8.txt") as f:
    data = f.readlines()
    data = [i[:-1] for i in data]
    data= [[int(i) for i in j ] for j in data]
    # data = [int(i) for i in data]

def get_col(matrix, j):
    return [row[j] for row in matrix]



def part1():
    n = len(data)
    m = len(data[1])
    visible = 2*((n - 1) + (m - 1))
    # print(data,n,m)
    for i in range(1, n-1):
        for j in range(1, m-1):
            # print(data[i][j])
            if(data[i][j] > max(data[i][0:j]) or data[i][j] > max(data[i][j+1:]) or data[i][j] > max(get_col(data,j)[0:i]) or data[i][j] > max(get_col(data,j)[i+1:]) ):
                # print(f"{data[i][j]} Vibibile in {i+1,j+1}")
                visible += 1
    return visible

# SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
# >>> max(a[1][0:3])
# 5
# >>> max(a[2][0:3])
# 6
# >>> max(a[2][1:3])
# 5

def get_view_score(m, i, j):
    rl = 0
    rr = 0
    cu = 0
    cd = 0
    for elem in m[i][j-1::-1]:
        if m[i][j] <= elem:
            rl += 1
            break
        elif m[i][j] > elem:
            rl += 1
    for elem in m[i][j+1:]:
        if m[i][j] <= elem:
            rr += 1
            break
        elif m[i][j] > elem:
            rr += 1

    for elem in get_col(m,j)[i-1::-1]:
        if m[i][j] <= elem:
            cu += 1
            break
        elif m[i][j] > elem:
            cu += 1

    for elem in get_col(m,j)[i+1:]:

        if m[i][j] <= elem:
            cd += 1
            break
        elif m[i][j] > elem:
            cd += 1


    # print(rl,rr,cu,cd)
    return rl*rr*cu*cd
    

def part2():
    n = len(data)
    m = len(data[1])
    massimo = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            massimo = max(get_view_score(data,i,j),massimo)
    return massimo



print(part1())
print(part2())
# print(get_view_score(data,3,2))
# print(data[3][1] > max(data[3][0:1]))
# print(data[3][1] > max(data[3][2:]))
# print(data[3][1] > max(get_col(data,1)[0:]))
# print(data[3][1] > max(data[3][0:1]))
