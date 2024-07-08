# str = 'venu'
# new_str=''
# for i in range(len(str)-1,-1,-1):
#     new_str+=str[i]
# print(new_str)

# for i in str:
#     new_str = 1+new_str
# print(new_str)


# def revers(v):
#     v = v[::-1]
#     return v
#
# v = "venu"
# a = revers(v)
# print(a)

def revers(str):
    new_str = ''
    # for i in range(len(str) - 1, -1, -1):
    #     new_str += str[i]
    for i in range(-1, -len(str)-1, -1):
        new_str += str[i]
    return new_str


str = "venu"
b = revers(str)
print(b)

