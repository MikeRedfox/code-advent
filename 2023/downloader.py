import datetime
import os

YEAR = datetime.datetime.now().year
DAY = datetime.datetime.now().day
DAY = 15


my_str = f'''
def part_one():
    with open('input/{DAY}.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\\n','')
        ss.append(temp)


    return

def part_two():

    with open('input/{DAY}.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\\n','')
        ss.append(temp)


    return



print(part_one())

'''
os.system(f'./downloader.sh {DAY} {YEAR}')

with open(f'day_{DAY}.py','w') as f:
    f.write(my_str)

