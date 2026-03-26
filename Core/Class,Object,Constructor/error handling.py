#1
#• Create a class Person whose constructor takes age as an argument. Raise a ValueError if the age is less than 0.
# class Person:
#
#     def __init__(self, age):
#         if age < 0:
#             raise ValueError("Age cannot be less than 0")
#         self.age = age
# try:
#     p1 = Person(25)
#     print(f"Person 1 age: {p1.age}")
#     p2 = Person(-5)
# except ValueError as e:
#     print(f"Caught error: {e}")
#
# try:
#     p3 = Person(30)
#     print(f"Person 3 age: {p3.age}")
# except ValueError as e:
#     print(f"Caught error: {e}")


#2
#• Write a function named find_length(obj) that uses a loop to calculate the
# length of the given object without using the built-in len() function. The
# function should return the calculated length if the object is iterable. If a
# non-iterable object such as an integer is passed, the function should raise and
# handle a TypeError, and print an appropriate error message explaining what
# happens when an integer is sent as input.




























#3
# Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to 100.

# class Student:
#     def __init__(self, marks=0):
#         self._marks = 0
#         self.set_marks(marks)
#
#     def set_marks(self, marks):
#         if not isinstance(marks, (int, float)):
#             raise ValueError("Marks must be a number (int or float).")
#         if marks < 0 or marks > 100:
#             raise ValueError(f"Marks must be between 0 and 100. Got {marks}.")
#         self._marks = marks
#
#     @property
#     def marks(self):
#         return self._marks
#
#
#
# print("=== Valid marks ===")
# try:
#     student1 = Student(85)
#     print(f"Student1 marks: {student1.marks}")
#     student1.set_marks(95)
#     print(f"Updated marks: {student1.marks}")
# except ValueError as e:
#     print(f"Error: {e}")
#
# print("\n=== Invalid marks (negative) ===")
# try:
#     student2 = Student(-5)
# except ValueError as e:
#     print(f"Error: {e}")
#
# print("\n=== Invalid marks (above 100) ===")
# try:
#     student1.set_marks(105)
# except ValueError as e:
#     print(f"Error: {e}")
#
# print("\n=== Invalid marks (string) ===")
# try:
#     student3 = Student("A")
# except ValueError as e:
#     print(f"Error: {e}")



#4
# Create a custom exception named InvalidAgeError. Create a class Voter with a
# method check_eligibility(age) that raises this exception if age is less than 18

# class InvalidAgeError(Exception):
#     pass
#
#
# class Voter:
#     def __init__(self, age):
#         self.age = age
#
#     def check_eligibility(self, age):
#         if age < 18:
#             raise InvalidAgeError("not eligible to vote")
#         return "eligible to vote"
#
#
#
# print("=== Testing Voter class ===")
#
# voter1 = Voter(20)
# try:
#     result = voter1.check_eligibility(20)
#     print(f"Age 20: {result}")
# except InvalidAgeError as e:
#     print(f"Error: {e}")
#
#
# test_cases = [16, 17, 10]
# for age in test_cases:
#     voter = Voter(age)
#     try:
#         result = voter.check_eligibility(age)
#         print(f"Age {age}: {result}")
#     except InvalidAgeError as e:
#         print(f"Age {age}: {e}")
#
# print("\n=== Using instance age ===")
#
#
#
# class VoterImproved:
#     def __init__(self, age):
#         self.age = age
#
#     def check_eligibility(self):
#         if self.age < 18:
#             raise InvalidAgeError("not eligible to vote")
#         return "eligible to vote"
#
#
# voter2 = VoterImproved(22)
# print(voter2.check_eligibility())






#5
# reate a class BankAccount with an attribute balance. Implement a method
# withdraw(amount) that raises an exception if the withdrawal amount is greater
# than the available balance.

# class InsufficientFundsError(Exception):
#     """Custom exception raised when withdrawal exceeds available balance."""
#
#     def __init__(self, balance, amount):
#         self.message = f"InsufficientFundsError: Cannot withdraw ${amount:.2f}. Available balance: ${balance:.2f}"
#         super().__init__(self.message)
#
#
# class BankAccount:
#     def __init__(self, initial_balance=0.0):
#         """
#         Initialize BankAccount with initial balance.
#         """
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")
#         self.balance = initial_balance
#
#     def deposit(self, amount):
#         """Deposit money into account."""
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self.balance += amount
#         print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
#
#     def withdraw(self, amount):
#         """
#         Withdraw money from account.
#         Raises InsufficientFundsError if amount > balance.
#         """
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             raise ValueError("Withdrawal amount must be a positive number.")
#
#         if amount > self.balance:
#             raise InsufficientFundsError(self.balance, amount)
#
#         self.balance -= amount
#         print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
#
#
#
# print("=== BankAccount Demo ===")
# account = BankAccount(1000.0)
#
#
# try:
#     account.withdraw(300)
#     account.deposit(200)
#     account.withdraw(500)
# except (InsufficientFundsError, ValueError) as e:
#     print(f"Error: {e}")
#
# print(f"\nFinal balance: ${account.balance:.2f}")
#
#
# print("\n=== Insufficient funds test ===")
# try:
#     account.withdraw(1000)
# except InsufficientFundsError as e:
#     print(e)









#6
#  Create a class PasswordValidator with a method validate(password). Raise an
# exception if the password length is less than 8 characters.



