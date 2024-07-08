class Student:
    col_name = "vagdeviTecnologies"

    def __init__(self):
        self.sid = 101
        self.sname = 'siva'

    @classmethod
    def col_info(cls):
        cls.col_add = "Ameerpeta"
        print(Student.col_name)
        print(cls.col_add)

    def std_info(self):
        print(Student.col_name)
        print(self.sid)
        print(self.sname)
        print(Student.col_add)

    @staticmethod
    def msg():
        print('hai')
        print("i am venu gopi")


s1 = Student()
s1.col_info()
Student.col_info()
s1.std_info()
s1.msg()
Student.msg()
