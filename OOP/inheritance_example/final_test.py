from Person import Person
from BabsonPerson import BabsonPerson
from Student import UG, Grad
from Professor import Professor

# TODO: add more testing code


def main():
    s1 = UG("Michael Vanikiotis", 2022)
    s2 = UG("Laura Ghouzi", 2022)
    s3 = UG("Brandon Chin", 2022)
    s4 = Grad("Matt Damon")
    s5 = UG("Mark Zuckerberg", 2021)
    p1 = Professor("Zhi Li", 'OIM 3640')
    p2 = Professor("Shankar", 'OIM 3690')
    p3 = BabsonPerson("Steve Gordon")
    q1 = Person("Bill Gates")
    q2 = Person("Beyonce")

    student_list = [s1, s2, s3, s5, s4]
    babson_list = student_list + [p1, p2, p3]
    all_list = babson_list + [q1, q2]

    # for everyone in student_list:
    #     print(everyone)

    # for everyone in babson_list:
    #     print(everyone)
    #     print(everyone.speak("Happy holidays!"))

    for everyone in all_list:
        print(everyone)


if __name__ == "__main__":
    main()
