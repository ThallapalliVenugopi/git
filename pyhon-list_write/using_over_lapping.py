from using_check_the import member


def over_lap(a, b):
    for temp in a:
        if member(b, temp):
            return True
    return False


a = [1, 2, 3, 4, 5, 6]
b = [10,8,9,0]
c = over_lap(a, b)
print(c)
