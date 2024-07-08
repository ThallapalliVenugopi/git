num=int(input("enter your numbe:"))
y=[]
for i in range (1,num+1):
    y.append(i)
print(y,end=' ')
y.insert(1,100)
print(y,end=' ')