# 1.
def check_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n) == c ** n:
        print("Holy smokes,Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def get_fermat():
    s = input("Input a,b,c and n for fermat check:")
    a, b, c, n = map(int, s.strip().split())
    check_fermat(a, b, c, n)


get_fermat()

# 2.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def get_bmi_category():
    s = input("Input weight and height:")
    weight, height = map(float, s.strip().split())
    print(calculate_bmi(weight, height))


get_bmi_category()
