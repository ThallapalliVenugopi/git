def swaplist(newlist):
    size = len(newlist)

    #one type swaping
    #temp = newlist[0]
    #newlist[0] = newlist[size - 1]
    #newlist[size - 1] = temp

    #second type of swaping
    #newlist[0], newlist[-1] =newlist[-1], newlist[0]

    #third typeo of swaping
    #start, *middle, end=newlist
    #newlist=[end, *middle, start]

    #fourth type swaping
    first=newlist.pop(0)
    last=newlist.pop(-1)
    newlist.insert(0,last)
    newlist.append(first)
    return newlist
newlist = [12,35,9,59,24]
print(newlist)
print(swaplist(newlist))
