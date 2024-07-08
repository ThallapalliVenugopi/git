try:
    x = 10
    y = int(input("enter your value:"))
    print(x / y)
except NameError:
    print("variable is not declaer")
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("cannot be divided by zero")
except:
    print("some thing went wrong")
else:
    print("no error")
finally:
    print('excutinon is end')

