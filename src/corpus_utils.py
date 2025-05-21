import numpy as np

from src.constants import ALPHABET

def _create_empty_dict(alphabet: str = ALPHABET):
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

def _create_count_dict(corpus: str, alphabet: str = ALPHABET):
    """
    Creates a nested dictionary counting how often each letter is followed by another
    letter in the given corpus.

    Args:
        corpus (str): The input text from which to count letter pairs.
        alphabet (str): A string of allowed characters. Defaults to 
                        ALPHABET defined at the module level.

    Returns:
        dict: A nested dictionary of the form {char_a: {char_b: count, ...}, ...},
              representing how often char_b follows char_a in the corpus.
    """
    count_dict = _create_empty_dict(alphabet=ALPHABET)
    for i in range(len(corpus) - 1):
        char_a = corpus[i]
        char_b = corpus[i+1]
        if char_a in alphabet and char_b in alphabet:
            count_dict[char_a][char_b] += 1
    return count_dict

def create_perc_dict(corpus: str, alphabet: str = ALPHABET):
    """
    Creates a nested dictionary of log-probabilities for each letter pair in the corpus.

    Args:
        corpus (str): The input text from which to estimate transition probabilities.
        alphabet (str): A string of allowed characters. Defaults to 
                        ALPHABET defined at the module level.

    Returns:
        dict: A nested dictionary of the form {char_a: {char_b: log_prob, ...}, ...},
              where log_prob is the natural logarithm of the smoothed probability
              that char_b follows char_a in the corpus.
    """
    perc_dict = _create_empty_dict(alphabet)
    count_dict = _create_count_dict(corpus, alphabet)
    for i in alphabet:
        total_count = sum(count_dict[i].values())
        for j in alphabet:
            letter_perc = (count_dict[i][j] + 1) / total_count
            perc_dict[i][j] = np.log(letter_perc)
    return perc_dict

def get_letter_frequencies(text: str, alphabet: str = ALPHABET):
    """
    Calculates the normalized frequency of each letter in a given text and returns them sorted by frequency.

    This function counts how often each character from the specified alphabet appears in the input text,
    normalizes the counts to get frequencies (as proportions of the total text length),
    and returns the letters and their frequencies sorted from most to least frequent.

    Args:
        text (str): The input string from which to calculate letter frequencies.
        alphabet (str, optional): A string containing valid characters to count.
                                  Defaults to the global `ALPHABET`.

    Returns:
        tuple:
            - letters (tuple): A tuple of letters sorted in descending order of frequency.
            - frequencies (tuple): A tuple of corresponding normalized frequencies (floats).
    """
    letter_freqency = {letter: 0 for letter in alphabet}
    for letter in text:
        if letter in alphabet:
            letter_freqency[letter] += 1

    letter_freqency = {key: value / len(text) for key, value in letter_freqency.items()}
    sorted_letters = sorted(letter_freqency.items(), key=lambda item: item[1], reverse=True)
    letters, frequencies = zip(*sorted_letters)
    return letters, frequencies
