import sys
import math

Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'


n = int(sys.argv[1])


def newton_binom(n):
    for i in range(n):
        row = []
        for j in range(i+1):
            coef = math.comb(i, j)
            if coef >= 1 and coef <= 9:
                row.append(Grey.format(coef))
            else:
                row.append(Blue.format(coef))
        print(' '.join(row).center(n*4))

newton_binom(n)


