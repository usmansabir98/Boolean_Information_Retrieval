import re

class QueryBuilder():
    def __init__(self, invertedIndex, query):
        self.ii = invertedIndex
        self.query = query

    def transformQuery(self):
        query = re.compile(re.escape('and'), re.IGNORECASE).sub('&', self.query)
        query = re.compile(re.escape('or'), re.IGNORECASE).sub('|', query)
        query = re.compile(re.escape('not'), re.IGNORECASE).sub('^', query)

        queryArray = query.split(" ")
        
        return queryArray

    def executeQuery(self):
        query = self.transformQuery()
        
        U = set([x for x in range(1,51)])
        s = ""
                
        for k,v in enumerate(query):
            
            if query[k-1] == '^':
                s += str(set(self.ii.getInvertedIndex(v.lower()))) + ')'
                
            elif v not in ['^', '&', '|']:
                s += str(set(self.ii.getInvertedIndex(v.lower()))) + ' '
                
            elif v=='^':
                s += '(U-'

            else:
                s += v

        docIds = eval(s)
        
        return {'docIds': docIds, 'documents': len(docIds)}
