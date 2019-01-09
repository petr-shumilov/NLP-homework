import nltk
from nltk.corpus import stopwords
import jamspell
import json
import logging
import traceback
from collections import defaultdict
from lib.Data import Data
from lib.Text import Text
from lib.Normalizer import Normalizer
import time



def main():

    ##
    ## lenght of subset
    SUBSET_AMOUNT = 20000
    ##
    ##

    handlers = [logging.StreamHandler()]
    logging.basicConfig(level = logging.INFO, 
                        format = '[%(asctime)s] %(levelname)s - %(message)s', 
                        handlers = handlers)
    logger = logging.getLogger('lemmatizer')


    logger.info("Preparing models...")
    corrector = jamspell.TSpellCorrector()
    corrector.LoadLangModel('resources/ru_small.bin')
    nltk.download('stopwords')


    logger.info("Data opening")
    data = Data('data/data.csv').open().read_as_csv(delimiter='\t')


    logger.info("Started")
    normalizer = Normalizer()
    lemmas = defaultdict(set)
    count = 0
    words_amount = 0
    start_time = time.time()

    for line in data:
        try:

            if count == SUBSET_AMOUNT:
                break

            text = Text(line[3])

            if text.detect_language() != 'ru':
                count += 1
                continue

            preprocessed_text = text.erase_punctuation() \
            .erase_stop_words() \
            .fix_spelling(corrector)

            for word in preprocessed_text.split():
                lemma = normalizer.lemmatize(word)
                lemmas[lemma].add(word)
                words_amount += 1 

        except Exception:
            pass
        finally:
            count += 1


    end_time = time.time()
    execution_time = end_time - start_time
    perf = float(words_amount) / float(execution_time)
    logger.info("Execution time: {}; Words: {}; Word per second: {}".format(execution_time, words_amount, perf))
    logger.info("Done!")

if __name__ == '__main__':
    main()

    