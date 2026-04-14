#1
#• Write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of
# characters in the file
# class Yogi:
#     def __init__(self,fn,m='r'):
#         self.fn=fn
#         self.m=m
#     def __enter__(self):
#         self.file=open(self.fn,self.m)
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exited the cm")
# with open("fg.py","r") as t:
#     t.seek(0)
#     c=0
#     for i in t:
#         c+=len(i)
#         print(c)
# with Yogi("fg.py","r")as yo:
#     print(yo.read())
from contextlib import contextmanager

#2
#  Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10
# characters.
# with open("fg.py",'r') as j:
#     lines=j.readlines()
#
#     for k in lines:
#         if len(k)>10:
#             print(k.rstrip('\n'))




#3
# Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints
# the complete file content.
# filename = "fg.py"
# with open(filename, "w") as file:
#     file.write("Line 1: This is the first line.\n")
#     file.write("Line 2: This is the second line.\n")
#     file.write("Line 3: This is the third line.\n")
# with open(filename, "a") as file:
#     file.write("Line 4: Appended fourth line.\n")
#     file.write("Line 5: Appended fifth line.\n")
#
# with open(filename, "r") as file:
#     content = file.read()
#     print(content)



#4
#  Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.
# filename="fg.py"
# with open(filename,"r") as file:
#     first_10=file.read(10)
#     print(f"print first 10 char:{first_10}")
#
#     pos=file.tell()
#     print(f"position of cuorser:{pos}")
#
#     begg=file.seek(0)
#     print(f"cursoe moved back position:{file.tell()}")




#5
# • Create a custom context manager using a class that opens a file in write mode
# in the __enter__ method, writes a line to the file, closes the file in the
# __exit__ method, and properly prints or logs any exception information received
# in __exit__.

# import traceback
#
# class SafeFileWriter:
#     def __init__(self, filename, line="Hello from custom context manager!\n"):
#         self.filename = filename
#         self.line = line
#         self.file = None
#
#     def __enter__(self):
#         print(f"Opening file: {self.filename}")
#         self.file = open(self.filename, "w", encoding="utf-8")
#         return self
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         if self.file:
#             print("Closing file.")
#             self.file.close()
#
#         if exc_type is not None:
#             print(f"An exception occurred: {exc_type.__name__}: {exc_value}")
#             print("Traceback (last few lines):")
#             traceback.print_tb(exc_tb, limit=5)
#         else:
#             print("File written successfully, no exceptions.")
#         return False
#
#
# # Usage example
# if __name__ == "__main__":
#     try:
#         with SafeFileWriter("test.txt") as writer:
#             writer.file.write(writer.line)
#             # 1 / 0
#     except Exception as e:
#         print("Outer handler caught:", e)







#6
#  Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object, and ensures the file is closed
# even if an exception occurs.


# from contextlib import contextmanager
#
# @contextmanager
# def open_file(fn, mode):
#     print("opening file")
#     f = open(fn, mode)
#     try:
#         yield f
#     finally:
#         f.close()
#         print("closing file")
#
# with open_file("test.txt", "w+") as f:
#     f.write("hello world")
#     f.seek(0)
#     print(f.read())
#
# with open_file("test.txt", "w+") as f:
#     print(f)