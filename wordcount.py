# import sys


# def word_count():
#     """Count words in file."""

#     word_file = open(sys.argv[1])

#     word_counts = {}

#     for each_line in word_file:
#         each_line = each_line.split()

#         for word in each_line:
#             word_counts[word] = word_counts.get(word, 0) + 1

#     for words, count in word_counts.items():
#         print(f"{words}: {count}")

# word_count()


def tokenize(source_file):
    """return a list of words from text at source_file"""

    word_file = open(source_file)
    words = []
    for each_line in word_file:
        each_line = each_line.split()

        for each_word in each_line:
            each_word = each_word.lower()
            if each_word[-1] == "." or each_word[-1] == "?" or each_word[-1] == "," or each_word[-1] == "!":
                each_word = each_word[:-1]
                words.append(each_word)
            else:
                words.append(each_word)

    return words

print(tokenize("test.txt"))


def count_words(list_of_words):
    """Take in a list of strings and return a dictionary"""
    """of each string and the number of times it appears in the list."""

    word_counts = {}

    for word in list_of_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(word_counts):
    """Take in a dictionary of word counts and print each key and value from"""
    """the dictionary"""

    for words, count in word_counts.items():
        print(f"{words}: {count}")
    