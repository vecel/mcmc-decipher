import numpy as np

from src import ALPHABET

def _create_empty_dict(alphabet=ALPHABET):
    """
    Creates empty dictionary for mapping following letters in the corpus text. 

    Args:
        alphabet (str): The string containing all letters in the alphabet.

    Return:
        dict: A dictionary mapping each letter from the alphabet to dictionary
            containing every letter.
    """
    empty_dict = {}
    for i in alphabet:
        for j in alphabet:
            empty_dict.setdefault(i, {})[j] = 0    
    return empty_dict

# TODO generate docstrings for functions below
def create_count_dict(corpus, alphabet):
    count_dict = _create_empty_dict(alphabet=ALPHABET)
    for i in range(len(corpus) - 1):
        char_a = corpus[i]
        char_b = corpus[i+1]
        if char_a in alphabet and char_b in alphabet:
            count_dict[char_a][char_b] += 1
    return count_dict

def create_perc_dict(count_dict, alphabet=ALPHABET):
    perc_dict = _create_empty_dict(alphabet)
    for i in alphabet:
        total_count = sum(count_dict[i].values())
        for j in alphabet:
            letter_perc = (count_dict[i][j] + 1) / total_count
            perc_dict[i][j] = np.log(letter_perc)
    return perc_dict

