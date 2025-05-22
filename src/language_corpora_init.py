from language_utils import create_lang_corpus, translate_queries 
import os
import asyncio
from constants import LANG_CODES

queries = ["Historia", "Geografia", "Internet", "Muzyka", "Literatura", "Sport", \
             "Natura", "Wydarzenia", "Polityka", "Taniec", "Zwierzęta", "Nauka", \
                "Człowiek", "Film", "Moda", "Architektura", "Religia"]

for lang_code in LANG_CODES:
    if lang_code != "pl":
        queries_t = asyncio.run(translate_queries(queries, src="pl", dest=lang_code))

    new_corpus = create_lang_corpus(lang_code, 10, queries_t)

    path = "../data/" + str(lang_code) + "_corpus.txt"

    if not os.path.exists(path):
        text_file = open(path)
        text_file.write(new_corpus)
        text_file.close()

# TODO check if it works   