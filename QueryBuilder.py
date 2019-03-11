import re

class QueryBuilder():
    def __init__(self, query, invertedIndex = None, positionalIndex = None):
        self.ii = invertedIndex
        self.pi = positionalIndex
        self.query = query

    def transformQuery(self):
        query = re.compile(re.escape('and'), re.IGNORECASE).sub('&', self.query)
        query = re.compile(re.escape('or'), re.IGNORECASE).sub('|', query)
        query = re.compile(re.escape('not'), re.IGNORECASE).sub('^', query)

        queryArray = query.split(" ")
        
        return queryArray

    def getIndex(self, word):
        if self.ii != None:
            index = self.ii.getInvertedIndex(word)
        elif self.pi != None:
            index = list(self.pi.getPositionalIndex(word).keys())
        else:
            index = []
        return index

    def executeQuery(self):
        query = self.transformQuery()
        
        U = set([x for x in range(1,51)])
        s = ""
    
        for k,v in enumerate(query):
            
            if query[k-1] == '^':
                index = self.getIndex(v.lower())
                s += str(set(index)) + ')'
                
            elif v not in ['^', '&', '|']:
                index = self.getIndex(v.lower())
                s += str(set(index)) + ' '
                
            elif v=='^':
                s += '(U-'

            else:
                s += v

        docIds = eval(s)

        return {'docIds': docIds, 'documents': len(docIds)}
            
