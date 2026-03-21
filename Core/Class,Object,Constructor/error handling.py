#1
#• Create a class Person whose constructor takes age as an argument. Raise a ValueError if the age is less than 0.
class Person:

    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be less than 0")
        self.age = age
p1=Person(25)
print(p1)