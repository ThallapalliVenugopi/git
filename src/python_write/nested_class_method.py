class Animal:
    legs=4
    class cat:
        def bark(self):
            print("cat's are having %d legs"%Animal.legs)
            print("cat's barking maew maew")
    class Dog:
        def bark (self):
            print("Dog's are having %d legs"%Animal.legs)
            print("dog's are barking bow bow")
a=Animal()
c=a.cat()
c.bark()
d=a.Dog()
d.bark()
