x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
y = {'sc': 92, 'eng': 91, 'tel': 32, 'hin': 71}

for i in x.items():
    print(i)
z=x.setdefault('venu01','india')
print(z)