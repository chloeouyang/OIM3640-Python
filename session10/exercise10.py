def exercise_01():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            letter += "u"
        print(letter + suffix)


# exercise_01()

team = "New England Patriots"


def exercise_02(word, letter):
    count = 0
    for x in word:
        if x == letter:
            count += 1
    return count


# print(exercise_02(team,'P'))


# print('www.example.com'.strip('cmo!#.w'))

# Whether the first letter of the string s is a lowercase letter.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# print(any_lowercase1(team))

# Whether letter c is a lowercase letter, and the answer is always True.
def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"


# print(any_lowercase2(team))

# Whether the last letter of the string s is a lowercase letter.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


# print(any_lowercase3(team))

# can't understand line 52
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# print(any_lowercase4(team))

# Whether the string s is filled with lowercase letter.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


# print(any_lowercase5(team))


def exercise_05(s, rotate_count):
    rotate_s = ""
    rotate_count = rotate_count % 26
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                letter = chr(((ord(letter) + rotate_count) - ord("a")) % 26 + ord("a"))
            else:
                letter = chr(((ord(letter) + rotate_count) - ord("A")) % 26 + ord("A"))
        rotate_s += letter
    return rotate_s


print(exercise_05("Gb trg gb gur bgure fvqr!", -13))
print(
    exercise_05(
        "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.",
        2,
    )
)
