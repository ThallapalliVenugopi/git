"using items metod= To return the list of items from the dict object"

# x = {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
# for i in x.items():
#     print(i)

def dic(x):
    for i in x.items():
        print(i)
    return i
x= {'m': 45, 'sc': 90, 'so': 32, 'tel': 87}
dic(x)