# sname=input("Enter your name:")
# for i in sname:
#     print(i,end="")
# x = sname.center(7)
# print(x)

def sname(name):
    for i in name:
        print(i,end="")
    return name
name="venu"
#print(name)
x=name.center(7,"@")
print(x)