class FiveDivisionError(Exception):
        pass


try:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    if num2 == 5:
        raise FiveDivisionError
    div = num1/num2
    print(div)
except (FiveDivisionError,ZeroDivisionError) as var:
    print(var,end='')
    print("cannot divided five and zero")
except ValueError:
    print("does not currect input")
except:
    print("some thing went wrong")
else:
    print("no error")
finally:
    print("rest of code")



