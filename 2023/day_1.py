import re
import itertools

def transform_string(input_string):
    num_dict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Create a list of words to be replaced
    words_to_replace = list(num_dict.keys())

    # Initialize an empty result string
    result = ''

    # Start iterating through the input string
    while input_string:
        # Find the first matching word from the list
        found = False
        for word in words_to_replace:
            if input_string.startswith(word):
                # Replace the word with its corresponding digit
                result += num_dict[word]
                # Remove the matched word from the input string
                input_string = input_string[len(word):]
                found = True
                break
        
        # If no match is found, move to the next character
        if not found:
            input_string = input_string[1:]

    return result

def part_one():

    with open('input/1.txt') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)

    somma = 0

    ss_n = []

    for word in ss:
        numero = ''
        for char in word:
            if char.isnumeric():
                numero += char
        ss_n.append(numero)

    for i in ss_n:
        somma += int(i[0]+i[-1])
        
    return somma

def part_two():
    with open('input/1.txt') as f:
        s = f.readlines()
    ss = []
    for i in s:
        temp = i.replace('\n','')
        ss.append(temp)



#     ss = ["two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2",
# "zoneight234",
# "7pqrstsixteen"]
    digits = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    ss_n = []


    for word_lunga in ss:
        temp = ''

        for i,c in enumerate(word_lunga):
            if c.isnumeric():
                temp += c
            for d,val in enumerate(digits.keys()):
                if word_lunga[i:].startswith(val):
                    temp += str(d)

        ss_n.append(temp)
    somma = 0
    for i in ss_n:
        somma += int(i[0] +(i[-1]))
    return somma
    # for i in range(len(ss)):
    #     print(ss[i],somma[i])

    # return sum([int(i) for i in somma])




print(part_two())