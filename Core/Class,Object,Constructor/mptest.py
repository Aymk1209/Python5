#test file
#1
# a=10
from os import strerror


#3
# def fun(a,b=0,c=0):
#     import mpcurrent
#     if (a > b and a>c):
#         print ("a is big")
#     elif b>c:
#         print("b is big")
#     else:
#         print('c is big')
# fun(3)





#6
# class Product:
#     def __init__(self, price):
#         if price <= 0:
#             print("Invalid Price")
#             self.__price = 0  # Default to 0 for invalid prices
#         else:
#             self.__price = price  # Set only if valid
#
#     @property
#     def price(self):  # Getter method
#         return self.__price
#
#     @price.setter
#     def price(self, value):  # Setter method
#         if value > 0:
#             self.__price = value
#             print(f"Price updated to ${value}")
#         else:
#             print("Invalid Price - must be positive")
#
#     def __str__(self):
#         return f"Product price: ${self.price}"





#7
# reuse_module.py

class BaseProcessor:
    def process_data(self, data):
        return f"Processed: {data.upper()}"
class InheritedProcessor(BaseProcessor):
    pass


class ComposedProcessor:
    def __init__(self):
        self.base = BaseProcessor()
    def process_data(self, data):
        return self.base.process_data(data)