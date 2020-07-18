##qustion = input("enter your number list")
##randomN = qustion.split(",")
##print(randomN)
##randomN.sort()
##print("sorted list",randomN)
##print(randomN[len(randomN)])
##print(randomN[0])
##
##


qustion = input("enter your number list")
randomN = qustion.split(",")

smallest = randomN[0]
largest = randomN[0]

for i in randomN:
    if(i > largest):
        largest = i
    if(i < smallest):
        smallest = i

print(f"largest = {largest}")
print(f"smallest = {smallest}")
