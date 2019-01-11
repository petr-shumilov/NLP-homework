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


def main():
    handlers = [logging.FileHandler("stemming.log"), logging.StreamHandler()]
    logging.basicConfig(level = logging.INFO, 
                        format = '[%(asctime)s] %(levelname)s - %(message)s', 
                        handlers = handlers)
    logger = logging.getLogger('stemming')


    logger.info("Preparing models...")
    corrector = jamspell.TSpellCorrector()
    corrector.LoadLangModel('resources/ru_small.bin')
    nltk.download('stopwords')


    logger.info("Data opening")
    data = Data('data/data.csv').open().read_as_csv(delimiter='\t')


    logger.info("Started")
    normalizer = Normalizer()
    #stemas = defaultdict(set)

    frequency = defaultdict(lambda: 0)
    count = 0


    for line in data:
        try:
            if count % 1000 == 0:
                logger.info("%d samples have been handled" % (count))
            if count % 20000 == 0:
                logger.info(json.dumps(stemas, 
                                        default=lambda x: list(x) if isinstance(x, set) else x.__dict__, 
                                        ensure_ascii=False))

            text = Text(line[3])

            if text.detect_language() != 'ru':
                count += 1
                continue

            preprocessed_text = text.erase_punctuation() \
            .erase_stop_words() \
            .fix_spelling(corrector)

            for word in preprocessed_text.split():
                stema = normalizer.stem(word)
                stemas[stema].add(word)
                frequency[stema] += 1

            count += 1
        except Exception as e:
            logger.error("Error: %s\nData: %s" % (str(e),(line[3] if len(line) >= 4 else line )))
            count += 1            
            


    logger.info(json.dumps(stemas, 
                            default=lambda x: list(x) if isinstance(x, set) else x.__dict__, 
                            ensure_ascii=False))
    logger.info(json.dumps(frequency, ensure_ascii=False))
    logger.info("Done!")
    logger.info("Amount of unique stemas: {}".format(len(frequency)))
    

if __name__ == '__main__':
    main()

    