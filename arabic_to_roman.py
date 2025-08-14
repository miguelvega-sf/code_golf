import sys

m = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

def r(i):
    o = ''
    n = int(i)
    for v, l in m:
        while n >= v:
            n = n - v
            o += l
    print(o)

with open(sys.argv[1], "r") as f:
    for l in f:
        r(l)