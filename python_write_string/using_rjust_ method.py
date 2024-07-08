# sname=input("Enter your name:")
# for i in sname:
#     print(i,end="")
# x=sname.rjust(7)
# print(x)

def sname(name):
    for i in name:
        print(i,end="")
    return name
name="venu"
#print(sname(name))
x=name.rjust(7,"$")
print(x)