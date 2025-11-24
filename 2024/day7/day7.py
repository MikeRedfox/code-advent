import itertools
import re


class calibrations:
    def __init__(self,input_string) -> None:
        self.res, self.nums = input_string.split(":")
        self.res = int(self.res)
        self.nums = [int(i) for i in self.nums.split(" ") if i!=""]

    def __str__(self) -> str:
        return(f"Risultato: {self.res}, Numeri: {self.nums}")

    def is_possible(self) ->bool:
        signs = list(itertools.product(["+","*"],repeat=len(self.nums)-1))
        risultati = []
        for val in signs:
            expressione = "("* (len(self.nums)-1)
            expressione += f"{self.nums[0]}"
            for i,sign in enumerate(val):
                expressione += f" {sign} {self.nums[i+1]})"
            # print(expressione)
            risultati.append(eval(expressione))
        return self.res in risultati


    def is_possible_with_concat(self) ->bool:
        signs = list(itertools.product(["+","*","||"],repeat=len(self.nums)-1))
        # risultati = []
        stringhe=[]
        for val in signs:
            expressione = f"{self.nums[0]}"
            for i,sign in enumerate(val):
                expressione += f"{sign}{self.nums[i+1]}"
            expressione = re.sub(r"\|\|","",expressione,10)
            numeri = re.findall(r"\d+",expressione)
            numeri = [int(n) for n in numeri]
            stringa_da_costr = f"{self.res}:"
            for j in numeri:
                stringa_da_costr += f" {j}"
            if stringa_da_costr not in stringhe:
                stringhe.append(stringa_da_costr)
            # temp = expressione.replace("||","")
            # print(temp)
            # risultati.append(eval(expressione))
        # print(stringhe)
        r = []
        for i in stringhe:
            r.append(calibrations(i).is_possible())
        return True in r

with open("/home/mike/scripts/code-advent/2024/input/day7.example") as f:
    data = f.readlines()
    data = [data[:-1] for data in data]
    
    
    print("- "*7)
    print(calibrations(data[4]).is_possible_with_concat())
    # BUG: Non funziona il codice, c'è un bug nel sito 😢
    print(calibrations("7290: 6 86 15").is_possible())
    # cal = sum([calibrations(i).res for i in data if calibrations(i).is_possible_with_concat()])
    # print(cal)
