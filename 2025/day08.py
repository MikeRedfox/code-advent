import math
from typing import override
from utils import get_data

data = get_data('./inputs/8_sample.txt')
# print(data)
class Point:
    def __init__(self,x: int,y: int,z: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z

    @override
    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.z}"

    def calculate_distance(self, otherPoint: "Point")-> float:
        res:float = math.sqrt((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2 + (self.z - otherPoint.z)**2)
        return res


points = []
distances = {}
for row in data:
    x,y,z = row.split(',')
    x = int(x)
    y = int(y)
    z = int(z)
    points.append(Point(x,y,z))

for idx,p in enumerate(points):
    for idx2,p2 in enumerate(points):
        if idx != idx2 and not distances.__contains__(f"{idx}-{idx2}") and not distances.__contains__(f"{idx2}-{idx}"):
                distances[f"{idx}-{idx2}"] = p.calculate_distance(p2)
        # distances.append(p.calculate_distance(p2))

distances_sorted = dict(
    sorted(distances.items(), key=lambda item: item[1])
)

k = []
for idx in distances_sorted.keys():
    print(idx, end="\t")

