def swapPosition(list, pos1, pos2):
    #one type
    #list[pos1], list[pos2] = list[pos2], list[pos1]

    #second type
    # first_ele = list.pop(pos1)
    # second_ele=list.pop(pos2)
    # list.insert(pos1,second_ele)
    # list.insert(pos2,first_ele)
    #third list
    get = list[pos1],list[pos2]
    list[pos1],list[pos2]=get
    return list

list = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(list)
print(swapPosition(list, pos1 - 1, pos2 - 1))
