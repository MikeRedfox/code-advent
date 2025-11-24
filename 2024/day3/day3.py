import re
from types import new_class


# 175700056
def part_one() -> int:

    # with open("/home/mike/scripts/code-advent/2024/input/day3.example") as f:
    with open("/home/mike/scripts/code-advent/2024/input/day3.txt") as f:
        data = f.readlines()[0]

    muls = re.findall(r"mul\(\d+,\d+\)",data)
    muls = [i[3:].replace("(","").replace(")","").split(",") for i in muls]
    # print(muls)
    res = sum([int(i)*int(j) for i,j in muls])
    return res

# 133100185
def part_two() -> int:

    # with open("/home/mike/scripts/code-advent/2024/input/day3.example") as f:
    with open("/home/mike/scripts/code-advent/2024/input/day3.txt") as f:
        data = f.readlines()[0]

    muls = re.sub(r"don't\(\)(.*?)do[^n]","",data,10000)
    muls = re.findall(r"mul\(\d+,\d+\)",muls)
    # print(new_muls)

    # print(muls)
    muls = [i[3:].replace("(","").replace(")","").split(",") for i in muls]
    # print(muls)
    res = sum([int(i)*int(j) for i,j in muls])
    return res


print("="*10)
# print(part_one())
print("Mia     Parte 2:",part_two())


from re import findall

total1 = total2 = 0
enabled = True
data = open("/home/mike/scripts/code-advent/2024/input/day3.txt").read()

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        total1 += x
        total2 += x * enabled

print("Giusta  Parte 2:",total2)

