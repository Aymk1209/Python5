# 1.  Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.
# class BankAccount:
#     def __init__(self, balance):
#
#         self.__balance = balance
#
#
#     def get_balance(self):
#         return self.__balance
#
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Deposited:", amount)
#         else:
#             print("Deposit amount must be positive")
#
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive")
#         elif amount > self.__balance:
#             print("Insufficient balance. Withdrawal denied.")
#         else:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#
#
# acc = BankAccount(1000)
#
# acc.deposit(500)
# acc.withdraw(300)
# print("Current Balance:", acc.get_balance())
# print("\nTrying to modify balance directly...")
#
# acc.__balance = 100000
# print("Balance after direct modification attempt:", acc.get_balance())
#
# print("\nActual object dictionary:", acc.__dict__)









# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states
#
# class Student:
#     def __init__(self, name: str, marks: int) -> None:
#         self.name = name
#         self.__marks = 0
#         self.update_marks(marks)
#
#     @property
#     def marks(self) -> int:
#         return self.__marks
#
#     def update_marks(self, new_marks:j int) -> None:
#         if not 0 <= new_marks <= 100:
#             raise ValueError("Marks must be between 0 and 100.")
#         self.__marks = new_marks
#
# s=Student("Yogi",85)
# s.marks = 120
# s.update_marks(5)
# s.__marks = 999
# s.update_marks(95)




# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)

# class SecureFile:
#     def __init__(self, content, password):
#         self.__content = content
#         self.__password = password
#         self.__log = []
#
#     def read(self, password):
#         if password == self.__password:
#             return self.__content
#         else:
#             self.__log.append("Unauthorized attempt")
#             return "Access Denied"
#
#
#
# file = SecureFile("This is secret data", "1234")
#
#
# print(file.read("1234"))
#
# print(file.read("0000"))
#
# print(file.__log)




#4.Design an Employee class where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent
# accidental downgrade)

#
# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary
#         self.__logs=[]
#
#     def get_salary(self):
#         self.__logs.append("Salary accessed")
#         return self.__salary
#
#
#     def update_salary(self, new_salary):
#         if new_salary > self.__salary:
#             self.__salary = new_salary
#             print("Salary updated")
#         else:
#             print("New salary must be higher than current salary")
#
#
# emp = Employee(30000)
#
#
# print(emp.get_salary())
#
#
# emp.update_salary(35000)
#
#
# emp.update_salary(20000)

# print(emp.__salary)  # This will cause an error





# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price().

# class Product:
#     def __init__(self,price,discount):
#         self.price=price
#         if self.price<=0:
#             print("Invalid Price")
#         self.__price=price
#
#         if discount>70:
#             raise ValueError("diss cant exced 70%")
#         self.__discount=discount
#     def __cal_final_price(self):
#         return self.price*self.__discount/100
#     def get_final_price(self):
#         return self.__cal_final_price()
# p1=Product(3000,65)
# print("Final prize:",p1.get_final_price())






#Create a Character class with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter

class Character:
    def __init__(self,health):
        self.__health=health


