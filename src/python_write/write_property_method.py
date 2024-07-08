# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("Getting value")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         print("setting value...")
#         if value < -273.15:
#             print("Temperature below -273 is not possible")
#         self._temperature = value
#
#
# human = Celsius(37)
# print(human.temperature)
# print(human.to_fahrenheit())
class House:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price,float):
            self._price=new_price
        else:
            print("please enter c valid price")
    @price.deleter
    def price(self):
        del self._price
h1=House(4000)
print(h1.price)
h1.price=50000.0
print(h1.price)
del h1.price
print(h1.price)


