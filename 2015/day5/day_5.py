def countVowels(s) -> int:
    i = 0
    for letter in s:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            i += 1
    return i


# https://www.geeksforgeeks.org/count-of-substrings-of-length-k-with-exactly-k-distinct-characters/


def wordContainsDouble(s) -> bool:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def containsBadSubstring(s) -> bool:
    for i in range(len(s) - 1):
        if (
            s[i : i + 2] == "ab"
            or s[i : i + 2] == "cd"
            or s[i : i + 2] == "pq"
            or s[i : i + 2] == "xy"
        ):
            return True
    return False


def isNiceString(s) -> bool:
    if countVowels(s) < 3:
        return False
    if not wordContainsDouble(s):
        return False
    if containsBadSubstring(s):
        return False
    return True


def part1():
    with open("../input/5.txt") as f:
        ipt = f.readlines()
    ipt = [word.replace("\n", "") for word in ipt]
    s = sum([1 if isNiceString(w) else 0 for w in ipt])
    return s


print(part1())
# print(isNiceString("dvszwmarrgswjxmb"))
