import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    pairs = sorted(hist.items(), key=lambda kv:kv[1], reverse=True)
    switch_pairs = []
    for pair in pairs:
        switch_pairs.append((pair[1], pair[0]))
    if not excluding_stopwords:
        return switch_pairs
    stopwords = []
    f = open("data/stopwords.txt")

    for line in f:
        word = line.strip()
        stopwords.append(word)

    exclude_pairs = []
    for pair in switch_pairs:
        if pair[1] not in stopwords:
            exclude_pairs.append(pair)
    
    return exclude_pairs


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    pairs = sorted(hist.items(), key=lambda kv:kv[1], reverse=True)
    for i in range(num):
        print(pairs[i][0], '\t', pairs[i][1])


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    for key in d2.keys():
        if key in d1:
            d1.pop(key)
    
    return d1


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    return random.choices(list(hist.keys()), list(hist.values()), k=1)[0]
    


def main():
    hist = process_file('data/Pride and Prejudice.txt', skip_header=True)
    print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    print_most_common(hist)

    words = process_file('data/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()