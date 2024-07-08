def generat_n_charecter(n, a):


    for i in range(n-1):
        a += a
    return a


n = 3
a = 'e'
c = generat_n_charecter(n, a)
print(c)
