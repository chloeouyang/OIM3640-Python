
def vowel_count(word):
    """
    Return the count of vowels(aeiou) in the given word.
    """
    count = 0
    for vowel in "aeiou":
        if vowel in word:
            count += 1

    return count


def has_duplicates(word):
    """
    Return True if any letter appears more than once in the word.
    """
    unique_set = set(word)
    # function set will generate a set without dunplicate element.
    # The return would be False if the word and the set has the same lenght.
    return not len(unique_set) == len(word)


def awesome_words():
    """
    Return how many words in the text file, drunkard_words.txt, are
    awesome words.

    Awesome words: words cantain at least three vowels, contain at least
    one letter that occurs twice in a row and have same first letter and
    last letter.
    """
    f = open('data/drunkard_words.txt')
    awesome_count = 0
    total_count = 0

    for line in f:
        total_count += 1
        word = line.strip()
        if vowel_count(word) > 3 and has_duplicates(
                word) and word[0] == word[-1]:
            awesome_count += 1

    return awesome_count, total_count


def main():
    print(vowel_count("pilot"))
    print(vowel_count("argumentsstream"))

    print(has_duplicates("appears"))
    print(has_duplicates("object"))

    awesome_count, total_count = awesome_words()
    print(
        f"The number of awesome words in the file drunkard_words.txt is {awesome_count}."
    )
    print(
        f"The percentage of the awesome words in the file drunkard_words.txt is {awesome_count/total_count*100:.2f}%."
    )


if __name__ == '__main__':
    main()