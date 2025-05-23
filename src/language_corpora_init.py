from language_utils import create_lang_corpus, translate_queries 
import os
import asyncio
from constants import LANG_CODES, FGN_ALPH
import json
from corpus_utils import create_perc_dict

queries = ["Historia", "Geografia", "Internet", "Muzyka", "Literatura", "Sport", \
             "Natura", "Wydarzenia", "Polityka", "Taniec", "Zwierzęta", "Nauka", \
                "Człowiek", "Film", "Moda", "Architektura", "Religia"]

for lang_code in LANG_CODES:
    # FIXME change absolute path to relative using os.getcwd()
    path = "/mnt/c/Users/user/Documents/AZŁM/mcmc-decipher/data/" + str(lang_code) + "_corpus.txt"
    
    if not os.path.exists(path):
        if lang_code != "pl":
            queries_t = asyncio.run(translate_queries(queries, src="pl", dest=lang_code))
        else:
            queries_t = queries    

        new_corpus = create_lang_corpus(lang_code, 10, queries_t)

        text_file = open(path, "w")
        text_file.write(new_corpus)
        text_file.close()

    path_dict = "/mnt/c/Users/user/Documents/AZŁM/mcmc-decipher/data/" + str(lang_code) + "_perc_dict.json"

    if not os.path.exists(path_dict):
        with open(path) as file:
            corpus = file.read()
        new_dict = create_perc_dict(corpus, FGN_ALPH[lang_code])

        with open(path_dict, "w") as outfile:
            json.dump(new_dict, outfile)    
