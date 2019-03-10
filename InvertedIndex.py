import re
from StopWords import StopWords

class InvertedIndex():
    def __init__(self):
        self.collection = [
            ['a','word','a','word','the'],
            ['the', 'a', 'brown', 'cat', 'the', 'a'],
            ['brown', 'cat', 'the', 'a', 'word']
        ]
        self.dictionary = {}
        self.stopWords = StopWords("D:/Information Retrieval/IR/stop words.txt")

    def loadDocuments(self):
        self.collection = []
        for i in range(1, 51):
            filename = "D:/Information Retrieval/IR/ShortStories/"+str(i)+".txt"
            s = ""
            with open(filename) as f_obj:
                for line in f_obj:
                    if(line != '\n'):
                        l = re.sub('[^a-zA-Z0-9\s]|[\n]', '', line)
                        l = self.stopWords.removeWords(l)
                        s = s + l.lower() + " "
            lines = s.split(" ")
            self.collection.append(lines)

    def buildDictionary(self):
        for i in range(0 ,len(self.collection)):
            array = self.collection[i]

            for j in range(0,len(array)):
                if(array[j] not in self.dictionary):
                    l = []
                    l.append(i+1)
                    self.dictionary[array[j]] = l
                else:
                    l = self.dictionary[array[j]]
                    l.append(i+1)
                    self.dictionary[array[j]] = l

        for key,value in self.dictionary.items():
            self.dictionary[key] = list(set(value))

    def getInvertedIndex(self, key):
        if key not in self.dictionary:
            return []
        return self.dictionary.get(key)
        
