import re

from InvertedIndex import InvertedIndex
from PositionalIndex import PositionalIndex
from QueryBuilder import QueryBuilder

class BooleanRetrieval():

    def __init__(self):
        self.ii = InvertedIndex()
        self.pi = PositionalIndex()

    def userInterface(self):
        op = '1'
        while(op!='0'):
            print("Boolean Information Retrieval")
            print("-----------------------------")
            print("1. Positional Index")
            print("2. Inverted Index")
            print("0. Exit")

            op = input("Enter input: ")

            self.inputQuery(op)

    def inputQuery(self, op):
        
        if op == '1':
            query = input("Enter query: ")
            self.pi.loadDocuments()
            self.pi.buildDictionary()
            self.printOutput(query)
            print("\n")
            
            
        elif op == '2':
            query = input("Enter boolean query: ")
            self.ii.loadDocuments()
            self.ii.buildDictionary()
            qb = QueryBuilder(self.ii, query)
            output = qb.executeQuery()
            print(output)
            print("\n")
        else:
            return

    def printOutput(self, query):
        print("query: ", query)
        dictionary = self.pi.getPositionalIndex(query)

        for k,v in dictionary.items():
            print("doc "+str(k)+":", v) 
        

br = BooleanRetrieval()
br.userInterface()
