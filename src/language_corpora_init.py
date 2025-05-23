from language_utils import create_lang_corpus, translate_queries 
import os
import asyncio
from constants import LANG_CODES, FGN_ALPH
import json
from corpus_utils import create_perc_dict

queries = ["Historia", "Geografia", "Internet", "Muzyka", "Literatura", "Sport", \
             "Natura", "Wydarzenia", "Polityka", "Taniec", "Zwierzęta", "Nauka", \
                "Człowiek", "Film", "Moda", "Architektura", "Religia", "Kosmos"]

for lang_code in LANG_CODES:
    path = "/mnt/c/Users/user/Documents/AZŁM/mcmc-decipher/data/" + str(lang_code) + "_corpus.txt"
    
    if not os.path.exists(path):
        if lang_code != "pl":
            queries_t = asyncio.run(translate_queries(queries, src="pl", dest=lang_code))
        else:
            queries_t = queries    

        new_corpus = create_lang_corpus(lang_code, 15, queries_t)
        with open(path, 'w') as textfile:
            textfile.write(new_corpus)

    path_dict = "/mnt/c/Users/user/Documents/AZŁM/mcmc-decipher/data/" + str(lang_code) + "_perc_dict.json"

    if not os.path.exists(path_dict):
        with open(path) as file:
            corpus = file.read()

        new_dict = create_perc_dict(corpus[0:2349663], FGN_ALPH[lang_code])
        with open(path_dict, "w") as outfile:
            json.dump(new_dict, outfile)  

# TODO run again - make corpora the same length after fixing create_perc_dict