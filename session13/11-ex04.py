dictionary = dict()


def store_dictionary():
    f = open('data/words.txt')

    for line in f:
        word = line.strip()
        dictionary[word] = 1


store_dictionary()
flag = dictionary.get("value", 0) == 1
print(f"value in the dictionary: {flag}")


def has_duplicates(t):
    d = dict()
    for item in t:
        if item in d:
            return True
        d[item] = 1
    return False


print(f"{has_duplicates([1, 2, 3])}")
print(f"{has_duplicates([1, 2, 3, 1])}")
