from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    f = open(file_path)
    file_info = f.read()

    return file_info


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi'): ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    for pos in range(len(words) - 1):
        key = (words[pos], words[pos + 1])
        value = None

        if pos != len(words) - 2:
            value = words[pos + 2]

        chains.setdefault(key, []).append(value)

    #print chains

    return chains


def check_concat_length(text, sentence):
    """checks the length if sentence is added and if <140 chars, adds it"""

    temp_sentence = text + ' ' + ' '.join(sentence)
    if len(temp_sentence) < 140:
        return temp_sentence
    else:
        return None


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here
    # end_var = 0
    # words = []
    sentence = []
    # print chains

    #this is a temp end point
    while len(text) < 140:
        key = choice(chains.keys())
        # print key

        while key[0] != key[0].title():
            key = choice(chains.keys())
            # print key
        #is there a better way to do this?
        sentence = [key[0], key[1]]

        value = choice(chains[key])

        if value is None:
            checked_length = check_concat_length(text, sentence)
            if checked_length is None:
                return text
            else:
                text = checked_length
                continue

        while True:
            sentence.append(value)
            if value[-1] in ['.', '!', '?']:
                checked_length = check_concat_length(text, sentence)
                if checked_length is None:
                    return text
                else:
                    text = checked_length

            key = (key[1], value)
            value = choice(chains[key])

            if value is None:
                break

        # while end_var < 50 and value[-1] not in ['.', '!', '?']:
        #     if value[-1] in ['.', '!', '?']:
        #         sentence.append(value)

        #     value = choice(chains[key])

        #     #here we want to be dealing with ends of sentences and making sure
        #     #we start with beginnigs next time

        #     #print value
        #     words.append(value)
        #     key = (key[1], value)
        #     end_var += 1
            
        #break
    text = ' '.join(words)
    return text


input_path = sys.argv[1]
#input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
#print input_text

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
