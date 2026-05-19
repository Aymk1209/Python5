# s="PYTHon"
# j=s.lower()
# print(j)
# k=s.upper()
# print(k)
# result = s.capitalize()
# print(result)
# t=s.title()
# print(t)
# sc=s.swapcase()
# print(sc)
from shlex import split

#length of string
# s="yogimanikanta"
# print(len(s))
    #or
# s="python"
# c=0
# for i in s:
#     c+=1
# print(c)


#ascii value
# s="yogi"
# for i in s:
#     print(ord(i))



#uppercase
# s="yogi"
# print(s.upper())

#lowercase
# s="MANI"
# print(s.lower())

#replace speces with -
# s="yogi"
# print("-".join(s))
     #or
# s="yogi is good boy"
# k=s.replace(" ","-")
# print(k)


#to find only digits in string
# s="23456789"
# print(s.isdigit())

#to find only alphas
# s="dfghjk"
# print(s.isalpha())

#to find num and alpha
# s="sdf1234"
# print(s.isalnum())


#write a program to validate aadhaar number
#
# n="1234 5678 9012"
# s=n.replace(" ","")
# if len(s)==12 and s.isdigit():
#     print("valid aadhaar number")
# else:
#     print("not valid aadhaar number")






#write a program to validate pan card








#write a program to validate gmail id using condition string
# def isuserValid(user):
#     if user[0].isAlpha():
#         return False
#     if user[-1]=="." or user[-1]=="_"
#         return False
#     for i in range(1,len(user)-1):
#        if not(user[i].isAlpha() or user[i].isdigit() or
#         user[i]=="." or user[i]=="_")
#         return False
#     return True
#
#
# g=input()
# l=len(g)
# if (l>=15 and l<=25):
#     uid=g.find("e")
#     user








#validate password based on len ,uppercase,lowercase,digit











#substring
# s="python pro gramming"
# d=input()
# if d in s:
#     print("yes exists")
# else:
#     print("not exist")

    #OR
# s=input()
# d=input()
# tl=len(d)
# for i in range(0,len(s)-tl):
#     if s[i:i+tl]==d:
#         print("Found")
#         break
# else:
#     print("Not found")





#finfing index of char
# s="python5"
# print(s.find("5"))


#find occerences of sepicif string
# s="yoyoyoyiii"
# print(s.count("i"))



#to find where the word is present in string
# s="python pro gramming"
# d=input()
# if d in s:
#     print(s.find(d))
# else:
#     print("not in string")
      #OR
# s=input()
# l=split(s)
# d=input()
# if d in l:
#     print("found")
# else:
#     print("not found")


#extract all digits from string
# s = "abc123def456gh789"
# digits = []
#
# for char in s:
#     if char.isdigit():
#         digits.append(char)
#
# print(''.join(digits))
# print(digits)

#Write a program to count the number of uppercase and lowercase letters in
#a string.
s=input()
uc=0
lc=0
for i in s:
    if i.upper():
        uc+=1
    else:
        lc+=1
print(uc)
print(lc)



#Write a program to separate alphabets, digits, and special characters from
#a string.
s=input()

