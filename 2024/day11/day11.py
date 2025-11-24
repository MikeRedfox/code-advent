from tqdm import tqdm

with open("/home/mike/scripts/code-advent/2024/input/day11.txt") as f:
    data = f.readlines()[0]
    data = [int(i) for i in data.split(" ")]

print("=" * 10)
print(data)


# blinks = 25
# for i in tqdm(range(blinks)):
#     numeri = []
#     for n in data:
#         if n == 0:
#             numeri.append(1)
#         elif len(str(n)) % 2 == 0:
#             mid = len(str(n)) // 2
#             n1 = int(str(n)[0:mid])
#             n2 = int(str(n)[mid:])
#             numeri.append(n1)
#             numeri.append(n2)
#         else:
#             numeri.append(n*2024)
#     data = numeri
#

# TODO: Capire la soluzione
cache = {}


def ans(x, n):
    if n == 0:
        return 1
    if (x, n) not in cache:
        if x == 0:
            result = ans(1, n - 1)
        elif len(str(x)) % 2 == 0:
            x = str(x)
            result = 0
            result += ans(int(x[: len(x) // 2]), n - 1)
            result += ans(int(x[len(x) // 2 :]), n - 1)
        else:
            result = ans(2024 * x, n - 1)
        cache[(x, n)] = result
    return cache[(x, n)]


res = 0
for x in data:
    res += ans(x, 75)

print(res)
