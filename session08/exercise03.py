import math


def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y

# print(mysqrt(25))

def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for i in range(1,10):
        a=int(i)
        b=mysqrt(a)
        c=math.sqrt(a)
        d=abs(b-c)
        print(f'{a}{b:<17.12}{c:<17.12}{d}')

test_square_root()

#question about aligning the data
