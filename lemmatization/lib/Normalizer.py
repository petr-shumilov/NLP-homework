from pymystem3 import Mystem   
from nltk.stem.snowball import SnowballStemmer
import re 

class Normalizer():
    def __init__(self):
        self.normalizer = Mystem()
        self.stemmer = SnowballStemmer('russian')

    def lemmatize(self, word):
        return self.normalizer.lemmatize(word)[0]

    def stem(self, word):
        return self.stemmer.stem(word)