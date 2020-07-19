

list1 = ["something", "trafford", "hall", "another", "word", "jeff"]
list2 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]



def firstThing(theList):
    return theList[0]
    
    
print( firstThing(list1))
print( firstThing(list2))


##################################


def lastThing(theList):
    a = len(theList)
    return theList[a - 1]
    


print( lastThing(list1))
print( lastThing(list2))



##################################
