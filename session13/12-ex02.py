def most_frequent(s):
    counts = dict()
    for word in s.split():
        for letter in word:
            if letter.isalpha():
                letter = letter.lower()
                cnt = counts.get(letter, 0)
                counts[letter] = cnt + 1
    print(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))


most_frequent(
    "Letter frequency is the number of times letters of the alphabet appear on average in written language."
)


def anagrams():
    f = open('data/words.txt')

    anagrams_dict = dict()
    anagrams_list = list()
    for line in f:
        word = line.strip()
        sort_word = str(sorted(word))
        if sort_word in anagrams_dict:
            anagrams_dict[sort_word].append(word)
        else:
            anagrams_dict[sort_word] = [word]

    for key, value in anagrams_dict.items():
        if len(value) > 1:
            anagrams_list.append(value)

    print(anagrams_list)


# anagrams()


def anagrams_sorted():
    f = open('data/words.txt')

    anagrams_dict = dict()
    for line in f:
        word = line.strip()
        sort_letters = sorted(word)
        sort_word = ''.join(sort_letters)
        if sort_word in anagrams_dict:
            anagrams_dict[sort_word].append(word)
        else:
            anagrams_dict[sort_word] = [word]

    for item in sorted(anagrams_dict.items(),
                       key=lambda kv: len(kv[1]),
                       reverse=True):
        if len(item[1]) == 1:
            break
        else:
            print(item[1])


# anagrams_sorted()