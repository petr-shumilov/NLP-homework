from pymystem3 import Mystem    

class Normalizer():
    def __init__(self):
        self.normalizer = Mystem()

    def lemmatize(self, word):
        return self.normalizer.lemmatize(word)[0]