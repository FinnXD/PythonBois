

def gimmeSomeSpace():
    print()
    print()


list1 = ["something", "trafford", "hall", "another", "word", "something"]
list2 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
list3 = ["something", "trafford", "hall", "hall", "trafford", "something"]
list4 = [1, 2, 3, 4, 3, 2, 1]

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
        
        
        


    
    

