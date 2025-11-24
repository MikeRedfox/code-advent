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
    print(data,n,m)
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

print(part1())

# print(data[3][1] > max(data[3][0:1]))
# print(data[3][1] > max(data[3][2:]))
# print(data[3][1] > max(get_col(data,1)[0:]))
# print(data[3][1] > max(data[3][0:1]))
