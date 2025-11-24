import numpy as np

with open("/home/mike/scripts/code-advent/2024/input/day25.example") as f:
    data = f.readlines()
    data = [i[:-1] for i in data]


print("=" * 10)
blocks = []
block = []
for elem in data:
    if elem != "":
        block.append(elem)
    else:
        blocks.append(block)
        block = []

keys = []
locks = []

for block in blocks:
    if block[0][0] == ".":
        keys.append(block)
    else:
        locks.append(block)

keys = np.array(keys)
locks = np.array(locks)


print(keys[0])
