# NOTE: Part 1: 17965282217
def process(secret: int, iterations=1) -> int:
    for _ in range(iterations):
        n = 64 * secret
        secret = secret ^ n
        secret = secret % 16777216
        t = secret // 32
        secret = secret ^ t
        secret = secret % 16777216
        t2 = secret * 2048
        secret = secret ^ t2
        secret = secret % 16777216

    return secret


print("-" * 10)
with open("/home/mike/scripts/code-advent/2024/input/day22.txt") as f:
    data = f.readlines()
    data = [int(i[:-1]) for i in data]

# print(data)
ns = [process(i, 2000) for i in data]
print(sum(ns))
