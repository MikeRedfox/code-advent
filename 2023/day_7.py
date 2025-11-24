def evaluate_hand(hand):
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 7, hand[0]
    if hand[0] != hand[1] != hand[2] != hand[3] != hand[4]:
        return 1,
    
    


def part_one():
    with open('input/7.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)

    #
    ss = [["32T3K", 765],
["T55J5", 684],
["KK677", 28],
["KTJJT" ,220],
["QQQJA" ,483]]

    ss_d = {k[0]:0 for k in ss}
    print(ss_d)
    print(evaluate_hand(ss[0][0]))



    return

def part_two():

    with open('input/7.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


    return



print(part_one())

