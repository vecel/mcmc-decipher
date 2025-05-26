import random

from src.constants import ALPHABET

def create_encryption_dict(alphabet: str = ALPHABET):
    """
    Creates random encryption dictionary for substitution cipher.

    Args:
        alphabet (str): The string containing all letters used in encryption.

    Returns:
        dict: A dictionary mapping each letter from the alphabet to a unique
              substitution letter (also from alphabet)
    """
    encryption_dict = {}
    list_chars = list(alphabet)
    random.shuffle(list_chars)
    rand_chars = "".join(list_chars)
    for i in range(len(alphabet)):
        encryption_dict[alphabet[i]] = rand_chars[i]
    return encryption_dict

def encode(text: str, encryption_dict: dict):
    """
    Encodes a message using a substitution cipher.

    Args:
        text (str): The message to be encoded.
        encryption_dict (dict): The dictionary used for encryption.

    Returns:
        str: The encrypted text.
    """
    text_list = list(text)
    for i in range(len(text_list)):
        new_char = encryption_dict[text_list[i]]
        text_list[i] = new_char
    new_text = "".join(text_list)
    return new_text

def decode(encoded_text: str, encryption_dict: dict):
    """
    Decodes a text encoded with a substitution cipher.

    Args:
        encoded_text (str): The encrypted text.
        encryption_dict (dict): The dictionary used for encryption.

    Returns:
        str: The decoded plain text.
    """
    decryption_dict = {v: k for k, v in encryption_dict.items()}
    return encode(encoded_text, decryption_dict)
