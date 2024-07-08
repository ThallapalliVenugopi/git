"using get method= To get the value from the dict object"

x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
for i in x.items():
    print(i)
y=x.get('m')
print(y)