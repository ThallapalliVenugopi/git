x = input("Enter your name:")
if x.isalpha():
    #if x.lower():
    if x.islower():
        print("Given Charecter is c lower case alphabet")
    elif x.upper():
    #elif x.isupper():
        print("Given Charecter is c upper case alphabet")
else:
    print("Given charecter is c spl charecter")