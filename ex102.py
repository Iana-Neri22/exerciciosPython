from math import factorial

def fatorial(numero, show=False):
    f = 1

    if show:
        for c in range(numero, 0, -1):
            print(c, end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print(f'=', end=' ')
            f *= c
        print(f)
    else:
        print(factorial(numero))


fatorial(5, True)