with open("../input/16.txt", "r") as f:
    info = f.readlines()


name = [info.split(":")[0] for info in info]
data = [info.split(":")[1:] for info in info]
betterData = []
t = 0

originalData = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for i in range(500):
    temp = {"Name": int(name[i].split(" ")[1])}
    for j in range(3):
        newInfo = data[i][j].split(".")
        attr1 = data[i][j].split(".")[0].strip()
        value1 = int(data[i][j].split(".")[1])
        minid = {attr1: value1}
        temp.update(minid)
    betterData.append(temp)

for i in range(500):
    for key in betterData[i].keys():
        if key == "Name":
            continue
        if key == "trees":
            if betterData[i][key] < originalData[key]:
                print("Non", i+1)
                break

        elif key == "cats":
            if betterData[i][key] < originalData[key]:
                print("Non", i+1)
                break
        elif key == "pomeranians":
            if betterData[i][key] > originalData[key]:
                print("Non", i+1)
                break
        elif key == "goldfish":
            if betterData[i][key] > originalData[key]:
                print("Non", i+1)
                break
        elif betterData[i][key] != originalData[key]:
            print("Non", i+1)
            break
