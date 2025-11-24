import re
import sys

import numpy as np
import robotClass

# Reading input
with open("/home/mike/scripts/code-advent/2024/input/day14.txt") as f:
    data = f.readlines()
    data = [i[:-1] for i in data]

print("=" * 10)
# print(data)
WIDTH = 101
HEIGHT = 103
grid = np.zeros((HEIGHT, WIDTH))
robots = []
for row in data:
    px, py, vx, vy = re.findall(r"^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$", row)[0]
    px, py, vx, vy = int(px), int(py), int(vx), int(vy)
    robots.append(robotClass.Robot(px, py, vx, vy))

def print_grid(grid: np.ndarray):
    # rs,cs = grid.shape
    gs = ""
    for r in grid:
        for elem in r:
            if elem == 0:
                gs +="."
            else:
                gs += "#"
        gs +="\n"
    print(gs)
    


def partOne():
    for _ in range(100):
        for r in robots:
            r.move()

    for r in robots:
        grid[r.py, r.px] += 1

    mw = WIDTH // 2
    mh = HEIGHT // 2
    q1 = grid[0:mh, 0:mw]
    q2 = grid[0:mh, mw + 1 :]
    q3 = grid[mh + 1 :, 0:mw]
    q4 = grid[mh + 1 :, mw + 1 :]

    return int(q1.sum() * q2.sum() * q3.sum() * q4.sum())

    # NOTE: Part 1: 230686500
np.set_printoptions(threshold=sys.maxsize)


# TODO: Risolvere questa parte
def partTwo():
    for _ in range(100):
        grid = np.zeros((HEIGHT, WIDTH))
        for r in robots:
            r.move()
            grid[r.py, r.px] += 1
        print(_+1)
        print_grid(grid)
        print("\n")


# print(partOne())
# partTwo()
print( partOne() )
