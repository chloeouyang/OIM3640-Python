# import os
# print(os.getcwd())


# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# print(line)


# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open("data/words.txt")  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    return not (("e" in word) or ("E" in word))


# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open("data/words.txt")
    has_no_e_count = 0
    total_count = 0

    for line in f:
        word = line.strip()
        total_count += 1
        if has_no_e(word):
            has_no_e_count += 1
    return has_no_e_count / total_count


# perc_no_e = find_words_no_e()
# print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in forbidden:
        if letter in word:
            return False
    return True


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def user_input_avoids():
    """
    print the number of words that don't contain any of the forbidden letters
    """
    forbidden = input("Input forbidden letters:")
    f = open("data/words.txt")
    avoids_count = 0

    for line in f:
        word = line.strip()
        if avoids(word, forbidden):
            avoids_count += 1
    print(f"The number of the words without forbidden letters is {avoids_count}")


# user_input_avoids()


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    f = open("data/words.txt")
    has_no_vowels_count = 0
    total_count = 0

    for line in f:
        word = line.strip()
        total_count += 1
        if avoids(word, "aeiou"):
            has_no_vowels_count += 1
    return has_no_vowels_count / total_count


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word:
        if not letter in available:
            return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    """"""
    f = open("data/words.txt")
    only_use_planet_count = 0

    for line in f:
        word = line.strip()
        if uses_only(word, "planet"):
            only_use_planet_count += 1
            print(word)
    return only_use_planet_count


# print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if not letter in word:
            return False
    return True


# please write test cases
# print(uses_all("planet","abc"))
# print(uses_all("planet","ael"))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open("data/words.txt")
    use_all_vowels_count = 0
    for line in f:
        word = line.strip()
        if uses_all(word, "aeiouy"):
            use_all_vowels_count += 1
    return use_all_vowels_count


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    for i in range(1, len(word)):
        if word[i] < word[i - 1]:
            return False
    return True


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    f = open("data/words.txt")
    abecedarian_count = 0
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            abecedarian_count += 1
    return abecedarian_count


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_using_recursion(word[1:])


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    index = 1
    while index < len(word) and word[index] >= word[index - 1]:
        index += 1
    if index >= len(word):
        return True
    else:
        return False


# print(is_abecedarian_using_while('abcdef'))
