# def f1():
#     for i in range(1,10+1):
#         if i%2==0:
#             yield i
# result=f1()
# for values in result:
#     print(values)
#
#
def f1():
   for i in range(1,10+1):
       if i%2==0:
           yield i
result=f1()
print(result.__next__())
print(result.__next__())