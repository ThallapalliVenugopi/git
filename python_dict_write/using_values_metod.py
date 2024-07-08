"using value method : to return list of all value method in dict object"

# x= {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
# for i in x.values():
#     print(i)


def dic(x):
    for v in x.values():
        print(v)
    return x
x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
dic(x)