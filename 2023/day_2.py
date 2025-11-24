def analyse_game(line):
    a, b = line.split(':')
    _, ID = a.split()
    ID = int(ID)
    b = b.split(';')
    for temp in b:
        games = temp.split(',')
        for game in games:
            _,quantity,colour = game.split(' ')
            quantity = int(quantity)

            if colour == 'red' and quantity > 12 or colour == 'green' and quantity > 13 or colour == 'blue' and quantity > 14:
                return ID
    return 0

def analyse_game_2(line):
    a, b = line.split(':')
    _, ID = a.split()
    ID = int(ID)
    b = b.split(';')
    r_a = []
    g_a = []
    b_a = []
    greens = []
    reds = []
    blues = []
    for temp in b:
        games = temp.split(',')

        for game in games:
            _,quantity,colour = game.split(' ')
            quantity = int(quantity)
            if colour == 'red':
                reds.append(quantity)
            if colour == 'green':
                greens.append(quantity)
            if colour == 'blue':
                blues.append(quantity)
    return max(reds) * max(greens) * max(blues)


def part_one():

    with open('input/2.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)

#     ss = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
# "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
# "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
# "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",]

    sol = []
    for line in ss:
        temp = analyse_game(line)
        sol.append(temp)
    
    soluz = 0

    for idx, val in enumerate(sol):
        if val == 0:
            soluz += idx + 1
    
    return soluz,set(sol)



def part_two():

    with open('input/2.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)

    

#     ss = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
# "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
# "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
# "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",]

    somma = 0
    for line in ss:
        somma += analyse_game_2(line)

    return somma


print(part_two())