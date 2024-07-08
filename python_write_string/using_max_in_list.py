# def mx_in_list(li):
#     ma = li[0]
#     for i in li:
#         if i > ma:
#             ma = i
#     return ma
#
#
# li = [1, 2, 3, 4, 5]
# print(mx_in_list(li))

n = [1, 2, 3, 4, 5]
temp = 0
for i in n:
    if i >= temp:
        n = i
print(n)
