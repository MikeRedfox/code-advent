stack1= "S,T,H,F,W,R".split(",")
stack2 = "S,G,D,Q,W".split(",")
stack3 = "B,T,W".split(",")
stack4 = "D,R,W,T,N,Q,Z,J".split(",")
stack5 = "F,B,H,G,L,V,T,Z".split(",")
stack6 = "L,P,T,C,V,B,S,G".split(",")
stack7 = "Z,B,R,T,W,G,P".split(",")
stack8 = "N,G,M,T,C,J,R".split(",")
stack9 = "L,G,B,W".split(",")
stacks = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
with open("./input/5.txt") as f:
    instructions = f.readlines()
    instructions = [i[:-1] for i in instructions]


def part1() -> str:
    for i in instructions:
        ins_split = i.split(" ")
        n = int(ins_split[1])
        fr = int(ins_split[3])
        to = int(ins_split[5])
        for j in range(n):
            stacks[to-1].append(stacks[fr-1].pop())

    return "".join([stack[-1] for stack in stacks])

def part2():
    s = ["".join(i) for i in stacks]
    print(s)
    for i in instructions:
        ins_split = i.split(" ")
        n = int(ins_split[1])
        fr = int(ins_split[3])
        to = int(ins_split[5])
        s[to-1] += s[fr-1][-n:]
        s[fr - 1] = s[fr -1][:len(s[fr-1])-n]
    
    return "".join([stack[-1] for stack in s])

# print(part1())
print(part2())
