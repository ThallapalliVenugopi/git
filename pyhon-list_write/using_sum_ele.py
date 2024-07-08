def sum(a):
    add = 0
    for i in a:
        add += i
    return add


a = [1, 2, 3, 4, 5]
b = sum(a)
print(b)