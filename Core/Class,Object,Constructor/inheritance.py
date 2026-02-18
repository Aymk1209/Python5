# class A:
#     z=30
#     def __init__(self, x):
#         self.x = x
#     @classmethod
#     def m2(cls):
#         print("this is a class method")
#     def m1(self):
#         print("this is a Instance method")
# class B(A):
#     def __init__(self, x,y):
#         super().__init__(x)
#         self.y=y
#     @classmethod
#     def m1(cls):
#         super().m2()
# obj=B(10,20)
# B.m1()
#
#
#
#
# class A:
#     def __init__(self, x):
#         print("inside class A")
#         self.x = x
# class B(A):
#     def __init__(self, x):
#         print("inside class B")
#         super().__init__(x)
# class C(A):
#     def __init__(self, x):
#         print("inside class C")
#         super().__init__(x)
# class D(B,C):
#     def __init__(self, x,y):
#         print("inside D")
#         super().__init__(x)
#         self.y=y
# obj=D(10,20)
# print(D.mro())#list
# # print(D.__mro__)#tuple



#1
#Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
#
# # Derived class
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
# # Demonstration
# a = Animal()
# d = Dog()
#
# a.sound()
# d.sound()




#2
#  Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super().

# class A:
#     def show(self):
#         print("hi")
# class B(A):
#     print("bye")
#     super().show()
# b1=B()
# b1.show()


#3
# Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.

# class A:
#     def display(self):
#         print("class name A")
# class B(A):
#     def display(self):
#         print("class name is B")
# class C(B):
#     def display(self):
#         print("class name is C")
# obj=C()
# obj.display()



#4
# Implement hierarchical inheritance using a base class Vehicle and two child
# classes Car and Bike, each defining a method wheels().
# class Vehicle:
#     def show(self,name):
#         self.name=name
#         print("vehicle name:",self.name)
# class Car(Vehicle):
#     def wheels(self):
#         print("car has 4 wheels")
# class Bike(Vehicle):
#     def wheels(self):
#         print("Bike as 2 wheels")
# c=Car()
# b=Bike()
#
# c.show("honda")
# c.wheels()
#
# b.show("tvs")
# b.wheels()




#5
#  Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs.

# class Employee:
#     def salary(self):
#         base_salary=30303
#         print("Employee salary:",base_salary)
# class Manger(Employee):
#     def salary(self):
#         base_salary=30303
#         incentive=1000
#         total_salary=base_salary+incentive
#         print("Manger salary:",total_salary)
# e1=Employee()
# m1=Manger()
#
# e1.salary()
# m1.salary()


#6
#Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.
# class University:
#     uni_name="CMR"
#     @classmethod
#     def m2(cls):
#          print("cm",cls.uni_name)
# class College(University):
#     def m3(self):
#         print("cc",College.uni_name)
# University.m2()
# College.m2()
#
# c1=College()
# c1.m2()



#7
# Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.

# class Mathops:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class AdvancedOps(Mathops):
#     pass
# m1=AdvancedOps.add(10,20)
# print(m1)


#8
#  Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO.
# class Father:
#     def skills(self):
#         print("he is dancer")
# class Mother:
#     def skills(self):
#         print("she is painter")
# class Child(Father,Mother):
#     pass
#
# c1=Child()
# c1.skills()



#10
# • Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor.

#
# class Person:
#     def __init__(self,name):
#         self.name=name
#         print("person constructor called")
# class Student(Person):
#     def __init__(self,name,roll):
#         super().__init__(name)
#         self.roll=roll
#         print("student constructor called")
# s1=Student("yogi",31)
# print(s1.name)
# print(s1.roll)






