num=int(input("enter your number:"))
x=set()
for i in range(1,num + 1):
    if i % 2 == 0:
        x.add(i)
print(x)
x.remove(10)
print(x)