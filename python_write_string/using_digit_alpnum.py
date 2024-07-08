x=input('enter your string: ')
if x.isalpha():
    if x.islower():
        print("Given string object contains only lowercase alphabets")
    elif x.isupper():
        print("Given string object contains only uppercase alphabets")
    else:
        print("Given string object contains both combination of lowercase and uppercase alphabets")
elif x.isdigit():
    print("given string object contains only digits")
elif x.isalnum():
    print("given string object contains both alphabets and digits")

else:
    print("Given string object contains not only alphabets and digits")


