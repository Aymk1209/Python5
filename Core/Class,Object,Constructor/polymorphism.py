#1
# Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().

# class Animal:
#     def make_sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def make_sound(self):
#         print("bow")
# class Cat(Animal):
#     def make_sound(self):
#         print("meow")
# class Cow(Animal):
#     def make_sound(self):
#         print("moo")
# animals=[Dog(), Cat(),Cow()]
# for animals in animals:
#     animals.make_sound()



# #2
# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine —
# all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type


# class Car:
#     def start(self):
#         print("Car starts with a key.")
#
#
# class Computer:
#     def start(self):
#         print("Computer boots up.")
#
#
# class WashingMachine:
#     def start(self):
#         print("Washing Machine starts washing.")
#
# def operate(device):
#     device.start()
# c1=Car()
# c2=Computer()
# wm=WashingMachine()
#
# operate(c1)
# operate(c2)
# operate(wm)


#03
# Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading
# gives natural polymorphism to user-defined classes.
# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#         # Overloading + operator
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#         # Overloading == operator
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = Vector(2, 3)
#
# # Using + operator
#
# print("v1 + v2 =", v1+v2)
#
# # Using == operator
# print("v1 == v2:", v1 == v2)
# print("v1 == v3:", v1 == v3)







#Q4. Create a base class Transport with move() and derived
# classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.

# class Transport:
#     def move(self):
#         print("vechel is moving")
#
# class Bus(Transport):
#     def move(self):
#         super().move()
#         print("bus carrys passengers")
#
# class Bike(Transport):
#     def move(self):
#         super().move()
#         print("bike goes fast")
#
# b1=Bus()
# b2=Bike()
#
# print("Bus movement:")
# b1.move()
#
# print("\nBike movement:")
# b2.move()







#Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.
# class Payment:
#     def process(self, amount):
#         print(f"Processing payment of {amount}")
# class CreditCardPayment(Payment):
#     def process(self, amount, card_type=None):
#         if card_type:
#             print(f"Processing {amount} using {card_type} credit card")
#         else:
#             super().process(amount)
# p = CreditCardPayment()
#
# p.process(1000)
# p.process(1000, "Visa")







#08. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again
# but calls parent using super()
# Show how polymorphism works across multiple levels.


# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
#         else:
#             print("Insufficient balance")
#
#
# class SavingsAccount(Account):
#     def withdraw(self, amount):
#         minimum_balance = 500
#         if self.balance - amount < minimum_balance:
#             print("Cannot withdraw. Minimum balance of 500 must be maintained.")
#         else:
#             super().withdraw(amount)
#
#
# class PremiumSavingsAccount(SavingsAccount):
#     def withdraw(self, amount):
#         print("Premium account withdrawal processing...")
#         super().withdraw(amount)
#
# accounts = [Account(5000),SavingsAccount(5000),PremiumSavingsAccount(5000)]
#
# for acc in accounts:
#     print("\nUsing:", acc.__class__.__name__)
#     acc.withdraw(4600)








#Q9. Create a function draw(shape) that works for objects
# of classes Circle, Square, and  Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car
# with draw() and pass it — what happens and why?


# class Circle:
#     def draw(self):
#         print("Drawing a Circle")
#
# class Square:
#     def draw(self):
#         print("Drawing a Square")
#
# class Rectangle:
#     def draw(self):
#         print("Drawing a Rectangle")
#
#
# class Car:
#     def draw(self):
#         print("Drawing a Car")
#
# def draw(shape):
#     shape.draw()
#
#
# c = Circle()
# s = Square()
# r = Rectangle()
# car = Car()
#
# draw(c)
# draw(s)
# draw(r)
# draw(car)










#08. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again
# but calls parent using super()
# Show how polymorphism works across multiple levels.

class Account:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f"with drawn amount {amount}, remaining: {self.balance}")
        else:
            print("Insufficent balance")
class SavingsAccount(Account):

    def withdraw(self,amount):
        min_balance = 500
        if self.balance-amount<min_balance:
            print("cant with draw min balance should be maitaiend")
        else:
            super().withdraw(amount)
class PreAcc(SavingsAccount):
    def withdraw(self,amount):
        print("premium acc withdraw processing")
        super().withdraw(amount)

accounts=[Account(5000),SavingsAccount(5000),PreAcc(5000)]

for acc in accounts:
    print(acc.__class__.__name__)
    acc.withdraw(4000)












# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
#         else:
#             print("Insufficient balance")
#
#
# class SavingsAccount(Account):
#     def withdraw(self, amount):
#         minimum_balance = 500
#         if self.balance - amount < minimum_balance:
#             print("Cannot withdraw. Minimum balance of 500 must be maintained.")
#         else:
#             super().withdraw(amount)
#
#
# class PremiumSavingsAccount(SavingsAccount):
#     def withdraw(self, amount):
#         print("Premium account withdrawal processing...")
#         super().withdraw(amount)
#
# accounts = [Account(5000),SavingsAccount(5000),PremiumSavingsAccount(5000)]
#
# for acc in accounts:
#     print("\nUsing:", acc.__class__.__name__)
#     acc.withdraw(4600)