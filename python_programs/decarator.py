class Student:
    col_name = " vagdivi"

    def __init__(self):
        self.sname = " venu gopi"
        self.sid = "101"

    @classmethod
    def col_info(cls):
        cls.col_add = "Guntur"
        print("col_name:", Student.col_name)
        print("col_add:", Student.col_add)
        print("col_add:", cls.col_add)

    def Stud_info(self):
        print("collge name:", Student.col_name)
        print("collge add:", Student.col_add)
        print("student name:", self.sname)
        print("Student sid:", self.sid)

    @staticmethod
    def msg():
        print("hai")
        x = 10
        print(x)


s1 = Student()
s1.col_info()
s1.Stud_info()
s1.msg()
