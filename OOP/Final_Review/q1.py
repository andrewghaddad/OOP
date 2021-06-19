def invert(d):
    #d is a dictionary
    #outputDict is the inverted dictionary
    outputDict = {}
    for i in d.keys():
        if(d[i] in outputDict.keys()):
            #if the key was already present append the value
            outputDict[d[i]].append(i)
        else:
            #if the key was not present in the outputDict
            #create a key and append the value
            outputDict[d[i]] = []
            outputDict[d[i]].append(i)
    #returns the outputDict
    return outputDict


#calling the function
d = {"Bob":"A","Alice":"A","Ted":"C","Halley":"B"}
print(invert(d))
