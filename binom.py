import sys
import math

n = int(sys.argv[1])

if n < 0:
    print('\033[91mInvalid parameter: n should be a positive integer\033[0m')
    sys.exit(1)

def binom(n):
    for i in range(n + 1):
        if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print('\033[90m', end="")
        else:
            print('\033[94m', end="")
        coef = math.comb(1, i)
        print(coef, end=" ")
    print('\033[0m')

binom(n)
