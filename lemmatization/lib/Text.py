import jamspell
import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
from langdetect import detect as detect_language
import re


class Text(str):

    def __new__(cls, value):
        obj = super().__new__(cls, value)
        return obj

    def erase_stop_words(self):
        # we are using 2 sources of stop words
        st_words1 = get_stop_words('russian')
        st_words2 = stopwords.words('russian')

        # and merging them
        stop_words = list(set(st_words2).union(set(st_words1)))
        
        return Text(' '.join([word for word in self.split() if word not in stop_words]))
        
    def erase_punctuation(self):
        return Text(re.sub(r'(.)(\1){2,}', r'\1', re.sub(r'[ ]{2,}', ' ', re.sub(r'[^а-яё\s]', ' ', self.lower()))).replace('ё', 'е'))

    def fix_spelling(self, corrector):
        return Text(corrector.FixFragment(self))

    def detect_language(self):
        return detect_language(self)