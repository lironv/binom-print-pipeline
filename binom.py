import sys
import math

n = int(sys.argv[1])


def newton_binom(n):
    for i in range(n):
        row = []
        for j in range(i+1):
            # Calculate the binomial coefficient using the math library
            coef = math.comb(i, j)
            # Color the output gray if the coefficient is between 1 and 9, otherwise blue
            if coef >= 1 and coef <= 9:
                row.append('\033[90m{}\033[0m'.format(coef))
            else:
                row.append('\033[94m{}\033[0m'.format(coef))
        print(' '.join(row).center(n*4))

# Prompt the user for input and call the function
n = int(input('Enter the number of rows for the Newton binomial triangle: '))
newton_binom(n)
