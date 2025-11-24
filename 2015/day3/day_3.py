def part1():
    with open("../input/3.txt") as f:
        puzzle_input = f.readlines()[0]

    # print(puzzle_input)

    temp = [0, 0]
    initial = [0, 0]
    init_set = []
    init_set.append(temp)
    for symbol in puzzle_input:
        # print(initial)
        if symbol == "^":
            initial[0] += 1
            if initial not in init_set:
                init_set.append(initial.copy())

        elif symbol == "v":
            initial[0] += -1
            if initial not in init_set:
                init_set.append(initial.copy())

        elif symbol == "<":
            initial[1] += -1
            if initial not in init_set:
                init_set.append(initial.copy())

        elif symbol == ">":
            initial[1] += 1
            if initial not in init_set:
                init_set.append(initial.copy())

    print(len(init_set))


def part2():
    # pz_inpt = "^v^v^v^v^v"
    with open("../input/3.txt") as f:
        pz_inpt = f.readlines()[0]


    santa = [0, 0]
    rbt_santa = [0, 0]
    rbt_santa_set =[]
    santa_set =[]
    santa_set.append(santa.copy())
    rbt_santa_set.append(rbt_santa.copy())
    it = 0
    for symbol in pz_inpt:
        if it % 2 == 0:
            if symbol == "^":
                santa[0] += 1
                if santa not in santa_set:
                    santa_set.append(santa.copy())
            elif symbol == "v":
                santa[0] += -1
                if santa not in santa_set:
                    santa_set.append(santa.copy())
            elif symbol == "<":
                santa[1] += -1
                if santa not in santa_set:
                    santa_set.append(santa.copy())
            elif symbol == ">":
                santa[1] += 1
                if santa not in santa_set:
                    santa_set.append(santa.copy())

        if it % 2 == 1:
            if symbol == "^":
                rbt_santa[0] += 1
                rbt_santa_set.append(rbt_santa.copy())
            elif symbol == "v":
                rbt_santa[0] += -1
                rbt_santa_set.append(rbt_santa.copy())
            elif symbol == "<":
                rbt_santa[1] += -1
                rbt_santa_set.append(rbt_santa.copy())
            elif symbol == ">":
                rbt_santa[1] += 1
                rbt_santa_set.append(rbt_santa.copy())
        it += 1

    all_set = []
    for i in santa_set:
        if i not in all_set:
            all_set.append(i)
    for i in rbt_santa_set:
        if i not in all_set:
            all_set.append(i)
    print(len(all_set))

# part1()
part2()
