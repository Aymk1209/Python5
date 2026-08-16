# #3
# from functools import reduce
# num=[5,10,15,20,25,30]
# result=reduce((lambda x,y:x**2 ),list)
# print(result)
# #
# #
# #
# #
# # #2
# # class Movie:
# #     total_movies=0
# #     def __init__(self,name,director):
# #         self.name=name
# #         self.director=director
# #     def new_formate(self,name,director):
# #
# #         print(name.split, director.split)
# #
# #1
# class LibraryMember:
#     max_limit=3
#     def __init__(self,member_name,books_borrowed):
#         self.member_name=member_name
#         self.books_borrowed=books_borrowed
#     def book(self,books):
#         if self.books_borrowed<LibraryMember.max_limit:
#             self.books_borrowed+=1
#             if not ValueError:
#                 print("not allowed to borrow the book")
#     @classmethod
#     def update(cls,new_limit):
#         LibraryMember.max_limit=new_limit
#     @staticmethod
#     def is_valid(requested):
#         if requested>0:
#             return True
#
# s1=LibraryMember("yogi",2)
# print(s1.book(4))
# s1.is_valid(3)
# print(s1.is_valid(4))



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #test-2... 5/3/16
# class Person:
#      def __init__(self,name,age,gender):
#          self.name=name
#          self.age=age
#          self.gender=gender
# class Account(Person):
#     def __int__(self,mail,password):
#         self.mail=mail
#         self.password=password
# class Instagram(Account):
#     accounts=[]
#     def __init__(self,mail,password):
#         self.accounts.append(mail)
#         super().__int__(mail,password)
# class Facebook(Account):
#     accounts=[]
#     def __init__(self,mail,password):
#         self.accounts.append(mail)
#         super().__int__(mail,password)
#
# j=Instagram("yogi",12)
# k=Facebook("mani",33)
# print(j.accounts)
# print(k.accounts)








#2
# class Vehicle:
#     def start(self):
#         print("hi")
# class Car(Vehicle):
#     def start(self):
#         print("bye car")
# class Bike(Vehicle):
#     def start(self):
#         print("bye bike")
# class Generator:
#     def start(self):
#         print("gen")
# class Machine:
#     def start(self):
#         print("mac")
#
# def start_machine(obj):
#     obj.start()
#
# v = Vehicle()
# c = Car()
# b = Bike()
# g = Generator()
# m = Machine()
#
# v.start()
# c.start()
# b.start()
# print("_______________________")
# start_machine(c)
# start_machine(b)
# start_machine(g)
# start_machine(m)



# #3
# class Employee:
#     def __init__(self,salary):



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#test3
#1
# class InsufficientBalance(Exception):
#     pass
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientBalance("Withdrawal amount exceeds available balance.")
#         self.balance -= amount
# d=BankAccount(10000)
# print(d.withdraw(1000000))








#3
# class ValueError(Exception):
#     pass
# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#         if self.price<0:
#             raise ValueError("no negative price")
#     def display_details(self):
#         print(f"book title: *{self.title}* /author name: *{self.author}* /price of book: *{self.price}*")
#
#
# c=Book("hi","yogi",500)
# c=Book("bye","mani",-10)
# print(c.display_details())




#
# #2
# class Member:
#     def __init__(self,username,credentials,perms):
#         self.username=username
#         self._credentials=credentials
#         self.__perms=[]
# class UserBase():
#     def get_role(self):









#2
#create class Service with a method that calls another method which
#raise an exception catch and handel the exception in the service class
# class NegativePriceError(Exception):
#     pass
#
# class Service:
#     def validate_price(self, price):
#         if price < 0:
#             raise NegativePriceError(f"Price cannot be negative.")
#         return price
#
#     def get_final_cost(self, price):
#         try:
#             return self.validate_price(price)
#         except NegativePriceError as e:
#             return f"Caught an exception: {e}"
#
# s1 = Service()
# print(s1.get_final_cost(100))
# print(s1.get_final_cost(-100))


#3
#abstract base class: Sensor with functions read_value()
#and calibrate()
#subclass:Temperaturesensor, pressuresensor, humiditysensor
#encapsulate:internal raw sensor readings print something
# which indicates type of sensor
#calibration factor log something which indicateds "calibration done successfully"
#hide all raw operations and allow only a public, clean get_reading() method
# from abc import ABC, abstractmethod
#
# class Sensor(ABC):
#     @abstractmethod
#     def _read_value(self):
#         pass
#
#     @abstractmethod
#     def _calibrate(self):
#         pass
#
#     def get_reading(self):
#         self._calibrate()
#         return self._read_value()
#
# class TemperatureSensor(Sensor):
#     def _read_value(self):
#         print("Reading from Temperature Sensor")
#         return 38
#
#     def _calibrate(self):
#         print("Temperature sensor: calibration done successfully")
#
# class PressureSensor(Sensor):
#     def _read_value(self):
#         print("Reading from Pressure Sensor")
#         return 100
#
#     def _calibrate(self):
#         print("Pressure sensor: calibration done successfully")
#
# class HumiditySensor(Sensor):
#     def _read_value(self):
#         print("Reading from Humidity Sensor")
#         return 60
#
#     def _calibrate(self):
#         print("Humidity sensor: calibration done successfully.")
#
#
# tem=[TemperatureSensor(), PressureSensor(), HumiditySensor()]
# for s in tem:
#     print(f"Output:{s.get_reading()}")














#2
# import threading
# counter=0
# lock = threading.Lock()
# def fun():
#     global counter
#     for i in range(1000000):
#         with lock:
#             counter+=1
#
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun)
# t1.start(); t2.start()
# # t1.join(); t2.join()
# print(counter)



#3
# class TypeErrorCustom(Exception):
#     pass
#
# class InvalidMarksError(Exception):
#     pass
#
# class StudentExam:
#     def __init__(self, student_name, subject, marks):
#         self.student_name = student_name
#         self.subject = subject
#         self.marks = marks
#     def add_marks(self, mark):
#         self.marks += mark
#     def calculate_result(self):
#         if type(self.marks) != int:
#             raise TypeErrorCustom("Marks should be an integer.")
#         if self.marks < 0 or self.marks > 100:
#             raise InvalidMarksError("Marks should be between 0 and 100.")
#         elif self.marks >= 40:
#             return "Pass"
#         else:
#             return "Fail"
#
# try:
#     s1 = StudentExam("yogi", "python", 85)
#     print(s1.calculate_result())
#
# except Exception as e:
#     print(e)
# try:
#     s2 = StudentExam("ram", "java", 120)
#     print(s2.calculate_result())
#
# except Exception as e:
#     print(e)
# try:
#     s3 = StudentExam("sai", "c", "90")
#     print(s3.calculate_result())
#
# except Exception as e:
#     print(e)


#1

# file="hi.py"
# with open(file,"r") as file:
#     first_10=file.read(10)
#     print(f"print first 10 char:{first_10}")
#
#     pos=file.tell()
#     print(f"position of cuorser:{pos}")
#
#     begg=file.seek(0)
#     print(f"cursoer moved back position:{file.tell()}")

































