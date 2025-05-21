import wikipedia
import time
from requests.exceptions import RequestException
import re

def create_lang_corpus(lang_code: str, n_results: int = 5, queries: list[str] = ["Internet"], max_retries: int = 5, backoff_factor: int = 2):
    """
    Retrieves and compiles the content of Wikipedia pages.

    Parameters:
        lang_code (str): The language code for Wikipedia (e.g., 'en' for English, 'pl' for Polish).
        n_results (int): The number of search results to consider for each query.
        queries (list): A list of search terms to query Wikipedia.
        max_retries (int): The maximum number of retry attempts for failed requests.
        backoff_factor (int): The multiplier for exponential backoff between retries.

    Returns:
        str: A concatenated string of the content from the retrieved Wikipedia pages, in lowercase.
    """
    if lang_code not in wikipedia.languages():
        lang_code = "pl"

    wikipedia.set_lang(lang_code)
    corpus = ""

    for query in queries:
        retries = 0
        while retries < max_retries:
            try:
                results = wikipedia.search(query, results=n_results)
                if not results:
                    raise ValueError(f"No results found for query: '{query}'")

                for result in results:
                    page = wikipedia.page(result)
                    corpus += page.content

                break

            except wikipedia.exceptions.HTTPTimeoutError:
                break
            except wikipedia.exceptions.RedirectError:
                break
            except wikipedia.exceptions.DisambiguationError:
                break
            except RequestException:
                pass
            except Exception:
                pass

            time.sleep((backoff_factor ** retries))
            retries += 1

    corpus = re.sub(r"[\(\[].*?[\)\]]", "", corpus)
    corpus = corpus.replace("=", " ")
    corpus = re.sub(r"\s+", " ", corpus)
    corpus = re.sub(r'\s*,\s*', ", ", corpus)
    corpus = re.sub(r'\s*\.\s*', ", ", corpus)
    return corpus.lower()

# TODO translate list of queries
# TODO create alphabet from corpus