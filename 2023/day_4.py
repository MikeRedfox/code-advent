
def part_one():
    with open('input/4.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


#     ss = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",]
    total_score = 0

    for line in ss:
        score = 0
        card, numbers = line.split(':')
        # _, ID = card.split(' ')
        # ID = int(ID)

        w_n, m_n = numbers.split('|')
        w_n = [int(i) for i in w_n.split(' ') if i != '']
        m_n = [int(i) for i in m_n.split(' ') if i != '']
        for n in m_n:
            if n in w_n and score == 0:
                score = 1
                continue
            if n in w_n and score != 0:
                score *= 2


        total_score += score






    return total_score

def part_two():

    with open('input/4.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)



    ss = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",]

    myD = {i:1 for i in range(1,len(ss)+1)}

    for line in ss:
        score = 0
        card, numbers = line.split(':')
        _, ID = card.split(' ')
        ID = int(ID)

        for _ in range(myD[ID]):

            w_n, m_n = numbers.split('|')
            w_n = [int(i) for i in w_n.split(' ') if i != '']
            m_n = [int(i) for i in m_n.split(' ') if i != '']
            winning_n = 0
            for n in m_n:
                if n in w_n:
                    winning_n += 1

            for i in range(ID,winning_n+2):
                myD[i+1] += 1

    print(myD)

    

    return



print(part_two())

