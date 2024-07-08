class Caluculation:
    def arith(self):  # instancemethod
        print('hai')

    @staticmethod
    def add(x, y):  # static Method
        print(x + y)
    # add(4,5)




c = Caluculation()
c.arith()
c.add(2, 5)
