import math

color=list(map(int,input().split()))#takes array input in a single line
counter=0   #counts individual color occurance in array
singlePair=0    #takes floor value of the total occurance of single color
totalPair=0     #for the addition of all color occurances

singleColor=list(dict.fromkeys(color))  #new array with no duplicate value
for x in range(len(singleColor)):   #for loop for counting
    counter=color.count(singleColor[x]) #calculating total occurances of single color
    singlePair=math.floor(counter/2)    #finding floor value
    if singlePair <0:
        pass
    else:
        totalPair=totalPair+singlePair #adding all the pair occurances
print(totalPair)
    
   
