"using from keys method = to assign values to the multiple keys at c time"

x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
for i in x.items():
    print(i)
y=x.fromkeys("siva",45)
print(y)
y=x.fromkeys(['ms','se','sw'],45)
print(y)
y=x.fromkeys(['ms','se','sw'],[45,23,43])
print(y)