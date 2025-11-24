
def part_one():
    seeds = [79, 14, 55, 13]
    seed_to_soil = [[50, 98, 2],[52, 50, 48]]
    soil_to_fert = [[0, 15, 37],[37, 52, 2],[39, 0 ,15]]
    fert_to_water = [[49, 53, 8],[0 ,11 ,42],[42 ,0 ,7],[57, 7, 4]]
    water_to_light = [[88, 18, 7],[18, 25, 70]]
    ligth_to_temp = [[45, 77, 23],[81, 45, 19],[68, 64 ,13]]
    temp_to_hum = [[0, 69, 1],[1, 0, 69]]
    hum_to_loc = [[60, 56, 37],[56, 93, 4]]

    



    return

def part_two():

    with open('input/5.txt','r') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)


    return



print(part_one())

