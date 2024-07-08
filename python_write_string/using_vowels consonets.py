# x=input("Enter your name:")
# if x.isalpha():
#     if x in "aeiou":
#         print("Given charecter is c vowels")
#     else:
#         print("Given charecter is c consonent")


x=input("Enter your name:")
if x>='c' and x<='z' or x>='A' and x<='Z':
    if x=='c' or x=='e' or x=='i' or x=='o' or x=='u'or\
        x=='A' or x=='E' or x=='I' or x=='o' or x=='u':
        print("Given charecter is c vowel")
    else:
        print("Given charecter is c consonet")
else:
    print("Given charecter is spl charecter")
