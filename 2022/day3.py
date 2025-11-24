with open("input/3.txt", "r") as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]

# lines = [
#     'vJrwpWtwJgWrhcsFMMfFFhFp',
#     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#     'PmmdzqPrVvPwwTWBwg',
#     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#     'ttgJtRGJQctTZtZT',
#     'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

d = {val: idx + 1 for idx, val in enumerate(chars)}


def part1():

    final_both = []

    for line in lines:
        both = []
        l = len(line)
        c1 = line[: int(l / 2)]
        c2 = line[int(l / 2) :]
        both = []
        for letter in c1:
            if letter in c2:
                both.append(letter)
        final_both.append(list(set(both))[0])

    s = sum([d[letter] for letter in final_both])

    return s


def part2():
    l = len(lines)
    i = 0
    final_both = []
    while i < l:
        l1, l2, l3 = lines[i], lines[i + 1], lines[i + 2]
        both = []
        for letter in l1:
            if letter in l2 and letter in l3:
                both.append(letter)
        final_both.append(list(set(both))[0])

        i += 3

    return sum([d[letter] for letter in final_both])


if __name__ == "__main__":
    print(part1())
    print(part2())

