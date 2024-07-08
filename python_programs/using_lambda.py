# add=lambda x,y:x+y
# print(add(4,5))

# using filter bultin function

# x=[1,2,3,4,5,6,7,8,9,10]
# even=filter(lambda i:i%2==0,x)
# for i in even:
#     print(i)

# using map bultin functon

# x=[1,2,3,4,5,6,7,8,9,10]
# even=map(lambda i:i%2==0,x)
# for i in even:
#     print(i)

# using import module

# from functools import reduce
#
# x = [1, 2, 3, 4, 5]
# print(reduce(lambda i, j: i + j, x))


x = list(map(lambda x: x % 2 == 0, range(20)))
print(x)
