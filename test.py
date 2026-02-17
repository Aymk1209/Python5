#3
from functools import reduce
num=[5,10,15,20,25,30]
result=reduce((lambda x,y:x**2 ),list)
print(result)
#
#
#
#
# #2
# class Movie:
#     total_movies=0
#     def __init__(self,name,director):
#         self.name=name
#         self.director=director
#     def new_formate(self,name,director):
#
#         print(name.split, director.split)
#













#1
class LibraryMember:
    max_limit=3
    def __init__(self,member_name,books_borrowed):
        self.member_name=member_name
        self.books_borrowed=books_borrowed
    def book(self,books):
        if self.books_borrowed<LibraryMember.max_limit:
            self.books_borrowed+=1
            if not ValueError:
                print("not allowed to borrow the book")
    @classmethod
    def update(cls,new_limit):
        LibraryMember.max_limit=new_limit
    @staticmethod
    def is_valid(requested):
        if requested>0:
            return True

s1=LibraryMember("yogi",2)
print(s1.book(4))
s1.is_valid(3)
print(s1.is_valid(4))







