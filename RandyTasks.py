

def gimmeSomeSpace():
    print()
    print()


list1 = ["something", "trafford", "hall", "another", "word", "something"]
list2 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
list3 = ["something", "trafford", "hall", "hall", "trafford", "something"]
list4 = [1, 2, 3, 4, 3, 2, 1]
list5 = ["jeff","jeff","bob","bob", "jeff", "jeff", "trafford","trafford","jeff","jeff"]




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
            print(newList)
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

######################################
        
    
        
