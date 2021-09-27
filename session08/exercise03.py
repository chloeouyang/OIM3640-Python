import math

def mysqrt(a):
    b=1/2
    sqrt=a**b
    return sqrt

print(mysqrt(25))

def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for i in range(1,10):
        a=int(i)
        b=mysqrt(a)
        c=math.sqrt(a)
        d=abs(b-c)
        print(f'{a:0}{b:14.12}{c:14.12}{d:10}')

test_square_root()