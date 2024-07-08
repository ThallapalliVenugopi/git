x = int(input("enter your first number:"))
y=set()
for i in range(1, x + 1):
    if i % 2 == 0:
        y.add(i)
print(y)
y.clear()
print(y)
