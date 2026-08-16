# #1
import threading
def add(a, b):
    print("Sum:", a + b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
t = threading.Thread(target=add, args=(a, b))
t.start()
t.join()
print("Main thread finished")



#2
# from contextlib import contextmanager
#
# @contextmanager
# def open_file(filename, mode):
#     f = open(filename, mode)
#     try:
#         yield f
#     finally:
#         f.close()
#
# with open_file("sample1.txt", "w") as file:
#     file.write("core python")



#3

class InsufficientBalanceError(Exception):
    pass
class User:
    def __init__(self, user_name, phone_num):
        self.user_name = user_name
        self.phone_num = phone_num
class Digital_Wallet(User):
    def __init__(self, user_name, phone_num, balance):
        super().__init__(user_name, phone_num)
        self.__balance = balance
    def add_money(self, amount):
        self.__balance += amount
    def pay_bill(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient Balance")
        self.__balance -= amount
        print("Bill Paid ")
    def show_balance(self):
        print("Balance:", self.__balance)c
u = Digital_Wallet("Yogi", "9876543210", 1000)
try:
    u.pay_bill(1200)
except InsufficientBalanceError as e:
    print(e)

u.show_balance()






















