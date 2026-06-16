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
# s=input()
# uc=0
# lc=0
# for i in s:
#     if i.upper():
#         uc+=1
#     else:
#         lc+=1
# print(uc)
# print(lc)



#Write a program to separate alphabets, digits, and special characters from
#a string.





#********palin**************

# def valid(x):
#     if x==x[::-1]:
#         return "palindrome"
#     else:
#
#         "not palindrome"






# s=input()
# l=s.split()
# d={"one":1, "two":2, "three":3, "four":4, "five":5 ,"six":6,   }
# for i in range(0,len(l)):
#     if l[i]=="double":
#         print(d[l[i+1]],end="")
#     elif l[i]=="triple":
#         print(d[l[i+1]],end="")
#         print(d[l[i+1]],end="")
#     else:
#         print(d[l[i]],end="")



#1>qwertyuiop
#2>asdfghjkl
#3>zxcvbnm

# def solution(s):
#     s=s.lower()
#     r1=set("qwertyuiop")
#     r2=set("asdfghjkl")
#     r3=set("zxcvbnm")
#     l=set(s)
#     if l.issubset(r1) or l.issubset(r2) or l.issubset(r3):
#         print("True")
#     else:
#         print("False")
# s=input()
# solution(s)




# 2>abc
# 3>def
# 4>ghi
# 5>jkl
# 6>mno
# 7>pqrs
# 8>tuv
# 9>wxyz
# input="kiran"
# 5+4+7+2+6=24
# output=24

# def solution(s):
#     d={ "abc":2,
#             "def":3,
#             "ghi":4,
#             "jkl":5,
#             "mno":6,
#             "pqrs":7,
#             "tuv":8,
#             "wxyz":9
#         }
#     t=0
#     for ch in s:
#         for key in d:
#             if ch in key:
#                 t+=d[key]
#     print(t,end=" ")
# s=input()
# solution(s)








# sub strings
# s=input().strip()
# cs=s.replace(" ","")
# len=0
# for _ in cs:
#     len+=1
# for i in range(len):
#     for j in range(i+1,len+1):
#         print(cs[i:j])



# s=input()
# cs=s.replace(" ","")
# k=int(input())
# for i in range(0,len(s)-k+1):
#     sub=s[i:i+k]
#     if k==len(sub):
#         print(sub)

# s=input()
# result=""
# for ch in s:
#     if ch not in result:
#         result+=ch
# print(result)


# s=input()
# t=input()
# c=0
# for i in range(0,len(s)-len(t)+1):
#     sub=s[i:i+len(t)]
#     if sub==t:
#         c+=1
# print(c)


#
# s=input()
# vowels="aeiouAEIOU"
# words=s.split()
# max_vowel_c=0
# word_wmv=""
# for word in words:
#     vowel_count=0
#     for ch in word:
#         if ch in vowels:
#             vowel_count+=1
#         if vowel_count>max_vowel_c:
#             max_vowel_c=vowel_count
#             word_wmv=word
# print(word_wmv)

# s=input()
# print(s+s)


# s=input()
# w=s.split()
# r=[]
# for ch in w:
#     r.append(ch[::-1])
# print(" ".join(r))


# palindrome
# def validPalindrome(s):
#     def isPalindrome(x):
#         return x == x[::-1]
#     if isPalindrome(s):
#         return "palindrome"
#     for i in range(len(s)):
#         new_string = s[:i] + s[i + 1:]
#         if isPalindrome(new_string):
#             return "palindrome"
#     return "not"
# print(validPalindrome("abca"))
# print(validPalindrome("raceacar"))
# print(validPalindrome("hello"))


# def validpalin(s):
#      def ispalin(x):
#          return x==x[::-1]
#      if ispalin(s):
#          return "palindrome"
#      for i in range(len(s)):
#          new_string=s[:i] +s[i+1:]
#          if ispalin(new_string):
#              return "palindrome"
#      return "not palindrome"






