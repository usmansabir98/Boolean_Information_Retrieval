collection = []

for i in range(1,5):
    filename = "D:/Information Retrieval/IR/ShortStories/"+str(i)+".txt"
    s = ""
    with open(filename) as f_obj:
        for line in f_obj:
            if(line != '\n'):
                s = s + line + " "
    lines = s.split(" ")
    collection.append(lines)


collection = [
    ['a','word','a','word','the'],
    ['the', 'a', 'brown', 'cat', 'the', 'a'],
    ['brown', 'cat', 'the', 'a', 'word']
]


dictionary = {}  

for i in range(0 ,len(collection)):
    array = collection[i]

    for j in range(0,len(array)):
        if(array[j] not in dictionary):
            docId = i+1
            d = {docId:[j]}
            dictionary[array[j]] = d
        else:
            d = dictionary[array[j]]

            if (i+1) in d:
                l = d[i+1]
                l.append(j)
                d[i+1] = l
                
            else:
                docId = i+1
                d[docId] = [j]
            
            dictionary[array[j]] = d
print("Dictionary")
print(dictionary)

print("\n\n Key 'word':")
print(dictionary['word'])

