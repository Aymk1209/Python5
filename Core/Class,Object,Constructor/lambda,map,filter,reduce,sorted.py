#1
# Use map() with a lambda to add 5 to every element of the following nested
# list [[1, 2], [3, 4], [5, 6]]
# nested_list=[[1,2],[3,4],[5,6]]
# result=list(map(lambda sublist:list(map(lambda x:x+5,sublist)),nested_list))
# print(result)


#2
#  Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
# filter() to keep only the keys whose values are greater than 50.

# d = {"apple": 100, "banana": 40, "cherry": 150}
# result=dict(filter(lambda item:item[1]>50,d.items()))
# print(result)


#3
#Use functools.reduce() with a lambda to find the largest number from a given
# list Dynamically

# from functools import reduce
# list=list(map(int,input("enter numbers:").split()))
# result= reduce(lambda x,y: x if x>y else y,list)
# print("larger num:",result)

#5th
#  Use map() on a string to convert each character into its ASCII value
# (using ord()). Print the result list.
# string=input(" ")
# result=list(map(ord,string))
# print(result)

#6th
# Use filter() to remove all vowels from a string and print the final string.
# text=input(" ")
# vowels= "aeiouAEIOU"
# result="".join(filter(lambda x:x not in vowels,text))
# print(result)

#7th
# Use reduce() to concatenate a list of characters into a single string.
# # Example input: ['P', 'y', 't', 'h', 'o', 'n'].
# from functools import reduce
# char=input("enter a separted charchters with space:").split()
# result=reduce(lambda x,y: x+y,char)
# print(result)

#8th
#   Given a list of integers, use map() with id() to print the memory address
# of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

# char=input("enter a separted numbers with space:").split()
# result=list(map(id,char))
# print(result)


#Use functools.reduce() with a lambda to find the largest number from a given
# list Dynamically

from functools import reduce
# list=list(map(int,input("enter numbers:").split()))
# result= reduce(lambda x,y: x if x>y else y,list)
# print("larger num:",result)

