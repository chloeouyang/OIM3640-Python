def gcd(a, b):
    if a < b:
        c = a
        a = b
        b = c
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b, c)


a, b = map(int, input("Input a and b for greatest common divisor:").strip().split())
print(gcd(a, b))
