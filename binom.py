import sys
import math

n = int(sys.argv[1])


def newton_binom(n):
    for i in range(n):
        row = []
        for j in range(i+1):
            coef = math.comb(i, j)
            if coef >= 1 and coef <= 9:
                row.append('\033[90m{}\033[0m'.format(coef))
            else:
                row.append('\033[94m{}\033[0m'.format(coef))
        print(' '.join(row).center(n*4))

newton_binom(n)
