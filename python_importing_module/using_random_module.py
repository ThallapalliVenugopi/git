y = [4, 2.3, 4j, False, "siva"]
import random

x = random.random()
print(x)
x = random.randint(1, 5)
print(x)
x = random.randrange(5)
print(x)
x = random.randrange(5, 10)
print(x)
x = random.randrange(1, 10, 2)
print(x)
x=random.choices(y)
print(x)
z=random.shuffle(y)
print(z)