from types import LambdaType


m0 = [79,98]
m1 = [54,65,75,74]
m2 = [79,60,97]
m3 = [74]

class Monkey:
    def __init__(self,start:list[int], operation: LambdaType,test: int,throw_true: int,throw_false: int) -> None:
        self.num_items_inspected = 0
        self.start = start
        self.operation = operation
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false

    def exec_round(self):
        new_items = []
        for item in self.start:
            self.num_items_inspected += 1
            x = self.operation(item)
            x //= 3
            if x % self.test == 0:
                monkeys[self.throw_true].start.append(x)
            else:
                monkeys[self.throw_false].start.append(x)
        self.start = new_items






mon0 = Monkey([79,98],lambda x: x*19,23,2,3)
mon1 = Monkey([54,65,75,74], lambda x: x+6,19,2,0)
mon2 = Monkey([79,60,97], lambda x: x*x,13,1,3)
mon3 = Monkey([74],lambda x: x+3,17,0,1)
monkeys = [mon0,mon1,mon2,mon3]


nr = 20
for i in range(nr):
    for m in monkeys:
        m.exec_round()

for m in monkeys:
    print(m.num_items_inspected)
