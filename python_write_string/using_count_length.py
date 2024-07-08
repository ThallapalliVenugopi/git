# # def length(a):
# #     count = 0
# #     for i in a:
# #         count += 1
# #     return count
#
# a = "venu"
# b = len(a)
# print(b)


def ma(a, b):
    for i in range(a - 1):
        b += b
    return b


a = 4
b = "s"
c = ma(a, b)
print(c)
