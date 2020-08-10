

def gimmeSomeSpace():
    print()
    print()


list1 = ["something", "trafford", "hall", "another", "word", "something"]
list2 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
list3 = ["something", "trafford", "hall", "hall", "trafford", "something"]
list4 = [1, 2, 3, 4, 3, 2, 1]
list5 = ["jeff","jeff","bob","bob", "jeff", "jeff", "trafford","trafford","jeff","jeff","barry","cole"]




#################################


def firstThing(theList):
    return theList[0]
    
    
print( firstThing(list1))
print( firstThing(list2))

gimmeSomeSpace()

##################################


def lastThing(theList):
    a = len(theList)
    return theList[a - 1]
    

print( lastThing(list1))
print( lastThing(list2))

gimmeSomeSpace()



##################################


def chooseThing(theList, p):
    return theList[p]

    
print( chooseThing(list1, 3))
print( chooseThing(list2, 5))

gimmeSomeSpace

####################################


def backToFront(theList):
    
    length = len( theList) - 1
    
    for i in range(length):
        
        print(f"this is the {i} time")
    
        b = length - i

        if theList[i] != theList[b]:
            return False

    return True
 


print (backToFront(list1))


print (backToFront(list3))
 
gimmeSomeSpace()

####################################

def checkdup (list5):
    newlist1 = []
    for i in range (len(list5)):
        for j in range (i + 1, len(list5)) :
            print(f"i is {i}")
            print(f"j is {j}")
            print() 
            
            if list5[i] == list5[j]:
                newlist1.append(list5[i])
    return newlist1
            
            

print(checkdup(list5))

gimmeSomeSpace()

####################################

def checkDupB (list5):
    newlist2 = [list5[0]]
    for i in range(1, len(list5)):
        a = i - 1
        print(a)
        if list5[a] != list5[i]:
            newlist2.append(list5[i])
    return newlist2


print(checkDupB(list5))

gimmeSomeSpace()

##################################


def dupsInList (list5):
    newList = [[list5[0]]]
    for i in range(1, len(list5)):
        
        a = i - 1
        if list5[a] != list5[i]:
            newList.append([list5[i]])
        else:
            newList[len(newList)-1 ].append(list5[a])
    return newList

print(checkDupB(list5))




print(dupsInList(list5) == [["jeff","jeff"],["bob","bob"], ["jeff", "jeff"], ["trafford","trafford"], ["jeff","jeff"]])    


gimmeSomeSpace()

####################################

def amountOfDups(startingList):
    finalList = []
    splitList = (dupsInList(startingList)) 
    for i in range (len(splitList)):
        a = len(splitList[i])
        finalList.append([a, splitList[i][0]])
    return finalList
        
print(amountOfDups(list5))

###################################


def amountOfDupsSingle(startingList):
    finalList = []
    splitList = (dupsInList(startingList)) 
    for i in range (len(splitList)):
        a = len(splitList[i])
        if a == 1 :
            finalList.append(splitList[i][0])
        else:
            finalList.append([a, splitList[i][0]])
    return finalList
        
print(amountOfDupsSingle(list5))

gimmeSomeSpace()
        
####################################    

def reverseDup(startingList):
    finalList = []
    for n in range (len(startingList)):
        numberInList = (startingList[n][0])
        actualWordInList = (startingList[n][1])
        currentList = []
        for i in range(numberInList):
            currentList.append(actualWordInList)
        finalList.append(currentList)
    return finalList


print(reverseDup(amountOfDups(list5)))

gimmeSomeSpace()

################################

def dupsdups(startingList, amount):    
    finalList = []
    firstThingInList = startingList[0]
    for n in range (len(startingList)):
        for i in range (amount):
            finalList.append(startingList[n])

        
        
    return finalList
    

    

oneList = ["a", "b", "c"]
print(dupsdups(oneList, 3) == ["a", "a", "a", "b", "b", "b", "c", "c", "c"])

print(dupsdups(oneList, 3))

####################################

def removeList(startingList, removedNumber):
    finalList = []
    for i in range (len(startingList)):
         if (i + 1) % removedNumber != 0:
            finalList.append(startingList[i])
            
            
            
        
    return finalList

randyList = [1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15]

print(removeList(randyList, 3))

gimmeSomeSpace()

######################################

def splitList(startingList,whereSplit):
    firstHalf = []
    secondHalf = []
    theRest = len(startingList) - (whereSplit)
    for i in range (whereSplit):
        firstHalfOfList = firstHalf.append(startingList[i])
    for n in range (theRest):
        secondHalfOfList = secondHalf.append(startingList[n+whereSplit])
    finalList = [firstHalf]+[secondHalf]
       
        
    return finalList
print(splitList(list5, 4))

#######################################

def chooseSplitList(startingList,placeOne,placeTwo):
    finalList = []
    firstBit = len(startingList) - (placeTwo)
    for i in range (len(startingList)):
        if i + 1 > (placeOne) and i < (placeTwo):
            finalList.append(startingList[i])

    return finalList

print(chooseSplitList(list5, 2, 7))





    
#def chooseSplitList(startingList,placeOne,placeTwo):
 #   finalList = []
  #  firstBit = len(startingList) - (placeTwo)
   # for i in range (firstBit):
    #    finalList.append(startingList[i+placeOne])

     

    #return finalList

#print(chooseSplitList(list5, 2, 1))







































    
        
        
    
    

