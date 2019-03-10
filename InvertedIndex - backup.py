collection = []

for i in range(1,5):
    filename = "D:/ir/ShortStories/"+str(i)+".txt"
    s = ""
    with open(filename) as f_obj:
        for line in f_obj:
            if(line != '\n'):
                s = s + line + " "
    lines = s.split(" ")
    collection.append(lines)

dictionary = {}  

for i in range(0 ,len(collection)):
    array = collection[i]

    for j in range(0,len(array)):
        if(array[j] not in dictionary):
            l = []
            l.append(i+1)
            dictionary[array[j]] = l
        else:
            l = dictionary[array[j]]
            l.append(i+1)
            dictionary[array[j]] = l

for key,value in dictionary.items():
    dictionary[key] = list(set(value))


#print(dictionary)

print(dictionary['brown'])
