import pickle


class Employe_name:
    def __init__(self, ename, eid, eaddres):
        self.ename = ename
        self.eid = eid
        self.eadress = eaddres

    def display(self):
        print("Employname:", self.ename)
        print("Employid:", self.eid)
        print("Employaddress:", self.eadress)


obj1 = Employe_name("venu", 101, '75 Tyallur')
obj2 = Employe_name("nage", 102, 'Guntur')
file = open("myfile", "wb")
pickle.dump(obj1, file)
pickle.dump(obj2, file)

file = open("myfile", 'rb')
obj1.display()
pickle.load(file)
obj2.display()
pickle.load(file)
