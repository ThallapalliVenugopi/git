def lenth(new_list):
    # first type
    # lent=len(new_list)
    # return lent

    # second type
    # if not new_list:
    #     return 0
    # return len(new_list)

    # third type
    if not new_list:
        return 0
    return 1 + lenth(new_list[1:])


# new_list = [1, 2, 3, 4, 5]
# print("the length of the list:", lenth(new_list))
