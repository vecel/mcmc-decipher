import random
import math
import numpy as np

from src.constants import ALPHABET
from src.cipher_utils import decode, create_encrytpion_dict

def score_likelihood(decoded_text: str, perc_dict: dict):
    """
    Computes the total log-likelihood score of a decoded text based on a transition model.

    Args:
        decoded_text (str): The text to evaluate (typically a decoded candidate message).
        perc_dict (dict): A nested dictionary where perc_dict[a][b] contains the
                          log-probability of character b following character a.

    Returns:
        float: The total log-likelihood score of the decoded text.
    """
    total_likelihood = 0
    for i in range(len(decoded_text) - 1):
        pair_likelihood = perc_dict[decoded_text[i]][decoded_text[i+1]]
        total_likelihood += pair_likelihood
    return total_likelihood

def shuffle_pair(current_dict: dict):
    """
    Creates a new substitution dictionary by randomly swapping two keys in the current one.

    Args:
        current_dict (dict): A dictionary representing a character substitution mapping.

    Returns:
        dict: A new dictionary with two randomly chosen values swapped.
    """
    a, b = random.sample(current_dict.keys(), 2)
    proposed_dict = current_dict.copy()
    proposed_dict[a], proposed_dict[b] = proposed_dict[b], proposed_dict[a]
    return proposed_dict

def eval_proposal(proposed_score: float, current_score: float):
    """
    Evaluates whether a proposed decryption should be accepted in the MCMC process.

    Args:
        proposed_score (float): Log-likelihood of the proposed decoding.
        current_score (float): Log-likelihood of the current decoding.

    Returns:
        bool: True if the proposal is accepted, False otherwise.
    """
    diff = proposed_score - current_score
    diff = min(1, diff)
    diff = max(-1000, diff)
    ratio = math.exp(diff)
    return ratio >= 1 or ratio > np.random.uniform(0,1)
    
def decode_MCMC(encoded_text: str, perc_dict: dict, iters: int, encryption_dict: dict = None, alphabet: str = ALPHABET, verbose: bool = False):
    """
    Attempts to decode a substitution cipher using a Markov Chain Monte Carlo (MCMC) approach.

    This function uses the Metropolis-Hastings algorithm to iteratively search for the most
    likely decryption of an encoded message. It begins with a random substitution mapping
    and proposes new mappings by swapping character pairs, accepting or rejecting each
    based on how the proposed decoding improves the log-likelihood under a language model.

    Args:
        encoded_text (str): The ciphertext to be decoded.
        perc_dict (dict): A nested dictionary of log-probabilities for character transitions,
                          typically created from a language corpus using `create_perc_dict()`.
        iters (int): Number of MCMC iterations to run.
        encryption_dict (dict): An encryption dictionary used as the starting point for the
                                algorithm. If not specified the random one will be used.
        alphabet (str): The character set used in the cipher and language model.
                        Defaults to the global `ALPHABET`.
        verbose (bool): If True, prints progress updates every 1000 iterations.

    Returns:
        tuple:
            - current_dict (dict): The final substitution mapping (best found).
            - best_score (list): List of scores recorded every 500 iterations.
            - best_text (list): List of corresponding decrypted texts
    """
    best_score = []
    best_text = []
    
    if encryption_dict is None:
        current_dict = create_encrytpion_dict(alphabet)
    else:
        current_dict = encryption_dict

    current_decrypted = decode(encoded_text, current_dict)
    current_score = score_likelihood(current_decrypted, perc_dict)
    
    for i in range(iters):
        proposed_dict = shuffle_pair(current_dict)
        proposed_decrypted = decode(encoded_text, proposed_dict)
        proposed_score = score_likelihood(proposed_decrypted, perc_dict)
    
        if eval_proposal(proposed_score, current_score):
            current_dict = proposed_dict
            current_score = proposed_score
            current_decrypted = proposed_decrypted
        
        if i % 500 == 0:
            best_score.append(current_score)
            best_text.append(current_decrypted)
        
        if verbose == True and i % 1000 == 0:
            print("Iteration: " + str(i) + ". Score: " + str(current_score) + '. Message: ' + current_decrypted[0:50])
            
    return current_dict, best_score, best_text

def cross_validation(attempts: int, encoded_text: str, perc_dict: dict, iters: int, encryption_dict: dict = None, alphabet: str = ALPHABET):
    # TODO add docstring
    all_scores = []
    all_samples = []
    for i in range(attempts):
        _, scores, samples = decode_MCMC(encoded_text, perc_dict, iters, encryption_dict=encryption_dict, alphabet=alphabet)
        all_scores.append(scores)
        all_samples.append(samples[-1])
    return all_samples, all_scores

def get_best_solution(all_samples: list[str], all_scores: list[list]):
    # TODO docstring
    max_score = float("-inf")
    max_idx = -1
    for i in range(len(all_samples)):
        score = all_scores[i][-1]
        if score > max_score:
            max_score = score
            max_idx = i
    return max_idx, max_score

def eval_solutions(text: str, all_solutions: list[str]):
    # TODO docstring
    correct = all_solutions.count(text)
    total = len(all_solutions)
    return correct / total
