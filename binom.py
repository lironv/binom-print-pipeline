from math import comb
import sys 


def newton_binom(num):
    try:
        num = int(num)
        if num < 0:
            raise ValueError
    except ValueError:
        print("\033[91mInvalid input: Please provide a non-negative integer.\033[0m")
        return

    for i in range(num + 1):
        if i <= 9:
            print(f"\033[90m{i}: {comb(num, i):,}\033[0m")
        else:
            print(f"\033[34m{i}: {comb(num, i):,}\033[0m")
            
n = int(sys.argv[1])
newton_binom(n)

