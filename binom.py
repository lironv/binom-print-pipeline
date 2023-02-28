from math import comb

def newton_binom(num):
    try:
        num = int(num)
        if num < 0:
            raise ValueError
    except ValueError:
        print("Invalid input: Please provide a non-negative integer.")
        return

    for i in range(num + 1):
        if i <= 9:
            print(f"{i}: {comb(num, i):,}")
        else:
            print(f"{i}: {comb(num, i):,}")

