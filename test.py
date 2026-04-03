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





#2
class Member:
    def __init__(self,username,credentials,perms):
        self.username=username
        self._credentials=credentials
        self.__perms=[]
class UserBase():
    def get_role(self):




