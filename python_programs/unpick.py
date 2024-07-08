import pickle


class employename:
    def __init__(self, ename, eid, eadress):
        self.ename = ename
        self.eid = eid
        self.eadress = eadress

    def dis(self):
        print("employ ename:", self.ename)
        print("employe eid:", self.eid)
        print("employe adress:", self.eadress)


file = open("pick", 'rb')
obj1 = pickle.load(file)
obj1.dis()
obj2 = pickle.load(file)
obj1.dis()
