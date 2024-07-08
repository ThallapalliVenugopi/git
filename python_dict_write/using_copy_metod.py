"using copy metod= To create c shallow copy  of c dict object"
x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
for i in x.items():
    print(i)
y=x.copy()
print(y)