# sname=input("enter your string name:")
# for i in sname:
#     print(i,end="")
# x=sname.count("i am")
# print(x)

def sname(name):
    for i in name:
        print(i,end="")
    return name
name="venu gopi i am from 75tyallur present i am in Guntur"
print(sname(name))
print(name.count("am"))
