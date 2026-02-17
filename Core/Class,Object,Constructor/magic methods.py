#__new__(cls):it gives address stores in x
# class A:
#     x=0
#     def __new__(cls):
#         if A.x== 0:
#             cls.x=super()
#         return cls.x
# obj=A()
# obj1=A()



#__call__:to call objects / we can callable objects
# class A:
#     def __call__(self,mrg):
#         print(mrg)
# obj=A()
# obj("hello")


#__contains__:we can coustomise the init /membership operation:
class Cvps:
    def __init__(self):
        self.students=[]
    def Addstudent(self,name):
        self.students.append(name)
    def __contains__(self, name):
        return name in self.students
obj=Cvps()
obj.Addstudent("yogi")



