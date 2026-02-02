# class Student:
#     total_students=0
#     def __init__(self,name):
#         self.name=name
#         Student.total_students+=1
#         print(f"new student has been created. Total students = {Student.total_students}")
# s1=Student("Narsimha")
# s2=Student("Devi")
from functools import total_ordering
from os import name


#we should get total amount of LOAN sholud be paid with intrest when we give the no. of months for 0.1 intrest
# class loan:
#     intrest=0.1
#     def __int__ (self,n,a):
#         self.name= n
#         self.amount=a
#     def total_amount(self,x):
#         return self.amount+(x*(self.amount*self intrest))
#


#1st
#Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

# class student:
#     def __init__ (self,name,marks):
#         self.name= name
#         self.marks= marks
#     def is_passed(self):
#         if self.marks>40:
#             print("passed")
#         else:
#             print("failed")
# #creating 2 objects
# student1=student("yogi",56)
# student2=student("mani",35)
#
# student1.is_passed()
# student2.is_passed()


#2nd
#Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
#.name=name
#         self.company_name="TechCrorp"
#     @classmethod
# class employee:
#     def __init__(self,name,company
#     def change_company(cls,new_name):
#         cls.company_name = new_name
# #create employes
# #soultion1:_name):
#         self
# e=employee("yogi")
#
# print(e.name,e.company_name)
#
# employee.change_company("cvcrorp")
# print(e.name,e.change_company)


#solution2
# class employee:
#     company_name = "TechCrorp"
#     def __init__(self,name,):
#         self.name=name
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name = new_name
# #create employes
# e=employee("yogi")
#
# print(e.name,e.company_name)
#
# employee.company_name=("cvcrorp")
# print(e.name,e.company_name)



#3rd
#Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.
#
# class mathops:
#     @staticmethod
#     def is_even(num):
#         if num%2==0:
#             return True
#         else:
#             return False
# obj=mathops
# print(obj.is_even(10))



#4th
#Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again

# class car:
#     wheels=4
#     def __init__(self, mileage):
#         self.mileage=mileage
#     def display_specs(self):
#         print("mileage:", self.mileage)
#         print("wheels:", car.wheels)
#     @classmethod
#     def change_wheels(cls,new_wheels):
#         cls.wheels= new_wheels
# car1=car(18)
# car1.display_specs()
# car1.change_wheels(6)
# car1.display_specs()



#5th
#Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.
#first tieal
# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     @staticmethod
#     def to_fahrenheit(celsius):
#         return(celsius*9/5)+32
#     def show_conversion(self):

#2nd tiral

# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     @staticmethod
#     def to_fahrenheit(celsius):
#         return(celsius*9/5)+32
#     def show_conversion(self):
#         fahrenheit = Temperature.to_fahrenheit(self.celsius)
#         print("celsius:", self.celsius)
#         print("fahrenheit:", fahrenheit)
# temp=Temperature(25)
# temp.show_conversion()

#6th
# Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created

# class Book:
#     total_books = 0  # class variable
#
#     def __init__(self, title, author):
#         if not Book.is_valid_title(title):
#             raise ValueError("Title must have at least 3 characters.")
#
#         self.title = title
#         self.author = author
#         Book.total_books += 1  # increment for every book created
#
#     @classmethod
#     def from_string(cls, book_str):
#         title, author = book_str.split("-")
#         return cls(title.strip(), author.strip())
#
#     @staticmethod
#     def is_valid_title(title):
#         return len(title) >= 3
#
#
# # Example usage
# b1 = Book("Python Basics", "John Doe")
# b2 = Book.from_string("AI-Andrew Ng")
#
# print(b1.title, b1.author)
# print(b2.title, b2.author)
# print("Total Books:", Book.total_books)






#7th
# Q7. Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0


# class Employee:
#     bonus_rate = 0.1
#     def __int__(self,name,base_salary):
#         self.name=name
#         self.base_salary = base_salary
#     def final_salary (self):
#         return self.base_salary+(self.base_salary * Employee.bonus_rate)
#     @classmethod
#     def update_bonus(cls, new_rate):
#         cls.bonus_rate = new_rate
#     @staticmethod
#     def is_valid_salary(sal):
#         if sal>0:
#             return True
#         else:
#             return False
# if Employee.is_valid_salary(100000):
#     emp1=Employee("yogi",100000)
# if Employee.is_valid_salary((40000)):
#     print(emp1.name,emp1.final_salary())
# Employee.update_bonus(0.2)
# print(emp1.name, emp1.final_salary())



#'''Q8. Create a class Course with:
# class variable total_students
# instance variable student_name
# instance method enroll() → increments total_students
# class method show_total(cls) → prints total students
# static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.''

# class Course:
#     total_students=0
#     def __init__(self,student_name,age):
#         self.student_name=student_name
#         self.age=age
#     def enroll(self):
#         Course.total_students+=1
#     @classmethod
#     def show_total(cls):
#         print(cls.total_students)
#     @staticmethod
#     def is_eligible(age):
#         if age >18:
#             return True
#         else:
#             return False
# s1=Course("yogi",22)
# s1.enroll()
# Course.show_total()
# print(Course.is_eligible(22))




#'''Q9. Create a class BankAccount with:
# class variable bank_name
# instance variables holder and balance
# instance method deposit(amount)
# class method change_bank_name(cls, new_name)
# static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together'''

# class BankAccount():
#     bank_name="UNION"
#     def __init__(self,holder,balance):
#         self.holder=holder
#         self.balance=balance
#     def deposit(self,amount):
#         if BankAccount.validate_amount(amount):
#             self.balance+=amount
#             print(f"{amount}deposited into{self.holder}account")
#             print("balance:",self.balance)
#         else:
#             print("Invalid deposit amount")
#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.change_bank_name=new_name
#         print("new bank name:", cls.change_bank_name)
#     @staticmethod
#     def validate_amount(amount):
#         if amount>0:
#             return True
# a1=BankAccount("yogi",3000)
# a1.deposit(10000)
# BankAccount.change_bank_name("sbi")
# print("account_holder:",a1.holder,"bank:",a1.change_bank_name)

#10th
#. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result


# class Student:
#     passing_marks = 40
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         if self.marks>=Student.passing_marks:
#             print(f"{self.name} is pass")
#         else:
#             print(f"{self.name} is fail")
#     @classmethod
#     def update_passing_marks(cls, new_marks):
#         cls.passing_marks=new_marks
#     @staticmethod
#     def grade_category(marks):
#         if marks>=75:
#             return "A"
#         elif marks>=60:
#             return "B"
#         else:
#             return "C"
# s1=Student("yogi",90)
# print("before updating passing marks:")
# print(s1.name,"grade:",Student.grade_category(s1.marks))
# s1.result()
#
# Student.update_passing_marks(70)
# print("After updating passing marks to 70:")
# print(s1.name,"grade:",Student.grade_category(s1.marks))
