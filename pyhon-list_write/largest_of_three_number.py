def lar_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a,b,c=5,1,2
lar = lar_of_three(a,b,c)
print(lar)
