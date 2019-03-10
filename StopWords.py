import re

class StopWords():
    def __init__(self, path):
        self.stopWords = []
        with open(path) as f_obj:
            for line in f_obj:
                self.stopWords.append(re.sub('\n', '', line))

    def removeWords(self, string):
        for word in self.stopWords:
            string.replace(word, '')
        string.replace('  ', ' ')
        return string
