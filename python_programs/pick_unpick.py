import pickle


class employename:
    def __init__(self, ename, eid, eadress):
        self.ename = ename
        self.eid = eid
        self.eadress = eadress

    def dis(self):
        print("employe ename:", self.ename)
        print("employe eid:", self.eid)
        print("employe adress:", self.eadress)


emp1 = employename("ravi", 101, "guntur")
emp2 = employename("malli", 102, "tyallur")
with open("pic_unpick", mode='wb') as f:
    pickle.dump(emp1, f)
    pickle.dump(emp2, f)

print("save successfully")

with open("pic_unpick", mode='rb') as f:
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
    obj1.dis()
    obj2.dis()



