def swapList(newlist):
    size=len(newList)


    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp

    return newList
newList=[22,4,5,56,7,88,9]
print(swapList(newList))
