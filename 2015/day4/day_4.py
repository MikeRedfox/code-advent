import hashlib


def part1():
    # r = hashlib.md5(b"abcdef")
    # print(r.hexdigest())
    for i in range(100_000, 10_000_000):
        s = ("ckczppom" + str(i)).encode("utf-8")
        r = hashlib.md5(s)
        if r.hexdigest()[0:6] == "000000":
            print(i)
    # s = ("abcdef" + str(609043)).encode("utf8")
    # r = hashlib.md5(s)
    # print(s)
    # print(r.hexdigest()[0:5] == "00000")


    # b'\xe8\x0bP\x17\t\x89P\xfcX\xaa\xd8<\x8c\x14\x97\x8e'
    # e80b5017098950fc58aad83c8c14978e


part1()
