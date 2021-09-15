def absolute(number):
    if number >= 0:
        print(number)
    else:
        print(-number)

absolute(182)
absolute(-999)

def my_abs(number):
    if number <0:
        return -number
    else:
        return number

print(my_abs(777))