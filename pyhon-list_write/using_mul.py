def mul(c):
    m = 1
    for i in c:
        m *= i
    return m


c = [1, 2, 3, 4, 5]
d = mul(c)
print(d)
