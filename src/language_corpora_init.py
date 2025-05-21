from language_utils import create_lang_corpus 
import os

queries = ["Historia", "Geografia", "Internet", "Muzyka", "Literatura", "Sport", \
            "Natura", "Wydarzenia", "Polityka", "Taniec", "Zwierzęta", "Nauka", "Człowiek"]

pl_corpus = create_lang_corpus('pl', 10, queries)

if not os.path.exists("../data/pl_corpus.txt"):
    text_file = open("../data/pl_corpus.txt", "w")
    text_file.write(pl_corpus)
    text_file.close()

# TODO other corpora    