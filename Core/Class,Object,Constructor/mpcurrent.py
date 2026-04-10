#1. Write a Python program that attempts to dynamically import a module at
# runtime. The program should only import the module if it actually exists;
# otherwise, it should print "Module does not exist".
# try:
#     import mptest as c
#     l=input()
#     print(c.a)
#     import mp as d
#     print(d.a)
# except ImportError:
#     print("Module does not exist")






#2.Create a Python package that contains two or more modules. Each module should
# define classes with attributes and methods. Then create another module outside
# the package, import the package modules, and create a subclass that inherits
# from at least one of the classes. Finally, create objects of both parent and
# child classes.
                        #and

##5 . Create three modules:
# Module A: class Animal
# Module B: class Walkable
# Module C: class Dog that inherits from both Animal and Walkable
# Demonstrate method resolution order (MRO) by calling overridden methods and
# printing the MRO.

#
# from petshop.animal25 import Animal
# from petshop.walkable25 import Walkable
#
#
# class Dog(Animal, Walkable):  # Multiple inheritance: Animal first, then Walkable
#     def __init__(self, name):
#         Animal.__init__(self, name, "Dog")
#         Walkable.__init__(self, 4)
#
#     def make_sound(self):
#         return f"{self.name} barks loudly!"
#
#     def walk(self):
#         return f"{self.name} trots on four paws"
#
#     def get_info(self):
#         return f"{Animal.get_info(self)} - {Walkable.get_info(self)}"
#
#
# # Parent objects
# animal = Animal("Generic", "Mammal")
# walkable = Walkable(4)
#
# print("=== Parent Objects ===")
# print("Animal:", animal.make_sound())
# print("Animal info:", animal.get_info())
# print("Walkable:", walkable.walk())
# print("Walkable info:", walkable.get_info())
# print()
#
# # Child object
# dog = Dog("Buddy")
#
# print("=== Child Dog Object (Multiple Inheritance) ===")
# print("Dog MRO:", Dog.__mro__)
# print("Dog make_sound():", dog.make_sound())
# print("Dog walk():", dog.walk())
# print("Dog get_info():", dog.get_info())
# print("Dog attributes:", vars(dog))






#3. Create two Python modules that import each other. Run the program to observe
# what happens with circular imports. Then think of different ways to prevent a
# circular-import crash.

# import mptest
# def fun(x):
#
#     x(50,70)
# fun(lambda x,y:print(x+y))







#4
# . Create a package with a module containing an abstract base class (ABC).
# Another module in the same package should define concrete subclasses that
# implement all abstract methods. Write a driver program that imports these
# classes and demonstrates polymorphism.
#
# from Animals.animal import Animal
# from Animals.dog import Dog
# from Animals.bird import Bird
#
# def demonstrate_behavior(animal: Animal):
#     """Polymorphic function using abstract base class."""
#     print(animal.speak())
#     print(animal.move())
#     print()
#
# # Create concrete subclass instances
# dog = Dog("Buddy")
# bird = Bird("Tweety")
#
# # Demonstrate polymorphism
# print("Polymorphism Demo:")
# demonstrate_behavior(dog)
# demonstrate_behavior(bird)

#6
# 6. Create a class in a module that uses private attributes and @property /
# @setter decorators. Import the class into another module and show how
# encapsulation protects the data while still allowing controlled access.


# from mptest import Product
#
# print("=== Testing Product Class Encapsulation ===")
#
#
# print("\\n1. Valid initial price:")
# p1 = Product(500)
# print(p1)
# print(f"Direct price access: ${p1.price}")
# print()
#
#
# print("2. Invalid initial price:")
# p2 = Product(-100)
# print(p2)
# print(f"Protected default price: ${p2.price}")
# print()
#
#
# print("3. Valid price update via setter:")
# p1.price = 750
# print(f"Updated price: ${p1.price}")
# print()
#
#
# print("4. Invalid price update (protected):")
# p1.price = -50
# print(f"Price unchanged: ${p1.price}")
# print()
#
# print("5. Direct private access (discouraged):")
# try:
#     print(p1.__price)
# except AttributeError as e:
#     print(f"Protected! {e}")
#
#
# print("\\n6. Protected convention access:")
# print(f"_Product__price: ${p1._Product__price}")



# 7. Create a module containing two classes where one uses composition and another
# uses inheritance to reuse code from a base class. Import and demonstrate the
# difference between the two approaches.
# demo.py
from mptest import InheritedProcessor, ComposedProcessor

# Test inheritance
inherited = InheritedProcessor()
print("Inherited:", inherited.process_data("hello"))  # Processed: HELLO

# Test composition
composed = ComposedProcessor()
print("Composed:", composed.process_data("hello"))    # Processed: HELLO

# Key runtime difference: identity check
print("Same type via inheritance?", isinstance(inherited, BaseProcessor))  # True
print("Same type via composition?", isinstance(composed, BaseProcessor))   # False