class Student:
    col_name="Vagdevi Technologies"
    col_add="Ameerpeta"
    def __init__(self):
        self.sid,self.sname=eval(input("enter your Student name: "))
    def std_info(self):
        print(f"Student Id:{self.sid},Student name:{self.sname},\
        College name:{Student.col_name},College Address:{Student.col_add}" )

t1=Student()
t1.std_info()
s2=Student()
s2.std_info()