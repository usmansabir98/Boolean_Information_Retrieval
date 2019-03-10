import re
from StopWords import StopWords

class PositionalIndex():
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
                        s = s + line + " "
            lines = s.split(" ")
            self.collection.append(lines)

    def buildDictionary(self):
        for i in range(0 ,len(self.collection)):
            array = self.collection[i]

            for j in range(0,len(array)):
                if(array[j] not in self.dictionary):
                    docId = i+1
                    d = {docId:[j]}
                    self.dictionary[array[j]] = d
                else:
                    d = self.dictionary[array[j]]

                    if (i+1) in d:
                        l = d[i+1]
                        l.append(j)
                        d[i+1] = l
                        
                    else:
                        docId = i+1
                        d[docId] = [j]
                    
                    self.dictionary[array[j]] = d

    def getPositionalIndex(self, key):
        if key not in self.dictionary:
            return []
        return self.dictionary.get(key)
        

#pi = PositionalIndex()
#pi.loadDocuments()
#pi.buildDictionary()
#print("word:", pi.getPositionalIndex('word'))
