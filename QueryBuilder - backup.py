from InvertedIndex import InvertedIndex
import re

ii = InvertedIndex()
ii.loadDocuments()
ii.buildDictionary()

query = input("Enter boolean query: ")

query = re.compile(re.escape('and'), re.IGNORECASE).sub('&', query)
query = re.compile(re.escape('or'), re.IGNORECASE).sub('|', query)
query = re.compile(re.escape('not'), re.IGNORECASE).sub('^', query)

query = query.split(" ")


U = set([x for x in range(1,51)])
s = ""
        
for k,v in enumerate(query):
    
    if query[k-1] == '^':
        s += str(set(ii.getInvertedIndex(v.lower()))) + ')'
        
    elif v not in ['^', '&', '|']:
        s += str(set(ii.getInvertedIndex(v.lower()))) + ' '
        
    elif v=='^':
        s += '(U-'

    else:
        s += v

docIds = eval(s)
print(docIds)
print("length ", len(docIds))
