import sys

m = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def r():
    for r in open(sys.argv[1]):
        o = ''
        n = int(r)
        for k in m:
            while n >= k:
                n = n - k
                o += m[k]
        print(o)
r()