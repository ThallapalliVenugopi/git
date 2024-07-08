"using pop method = to remove particuler item from the dict object"

x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
for i in x.items():
    print(i)
    print(x.pop('m'),i)

