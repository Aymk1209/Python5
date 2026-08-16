# 1. Print numbers in a given range using recursion
# def print_range(start, end):
#     if start > end:
#         return
#     print(start, end=" ")
#     print_range(start + 1, end)
#
# a = int(input("Enter start: "))
# b = int(input("Enter end: "))
#
# print_range(a, b)



# 2. Print all digits in a given number using recursion
# def print_digits(n):
#     if n == 0:
#         return
#     print_digits(n // 10)
#     print(n % 10)
#
# num = int(input("Enter number: "))
#
# if num == 0:
#     print(0)
# else:
#     print_digits(num)



# 3. Check whether a number is prime using recursion
# def is_prime(n, i=2):
#     if n <= 1:
#         return False
#     if i * i > n:
#         return True
#     if n % i == 0:
#         return False
#     return is_prime(n, i + 1)
#
# num = int(input("Enter number: "))
#
# if is_prime(num):
#     print("Prime")
# else:
#     print("Not Prime")


# def prime(n,c,i):
#     if i>n:
#         if c==2:
#             print("prime")
#         else:
#             print("no prime")
#         return
#     if n%i==0:
#         c+=1
#     prime(n,c,i+1)
# prime(17,0,8)




# 4. Print all even numbers in a given range using recursion
# def print_even(start, end):
#     if start > end:
#         return
#     if start % 2 == 0:
#         print(start, end=" ")
#     print_even(start + 1, end)
#
# a = int(input("Enter start: "))
# b = int(input("Enter end: "))
#
# print_even(a, b)




# def digit(n,sum):
#     if n==0:
#         print(sum)
#         return
#     sum+=n%10
#     digit(n//10,sum)
#
# digit(94,0)


# 5. Count even numbers in a given range using recursion
# def count_even(start, end):
#     if start > end:
#         return 0
#     if start % 2 == 0:
#         return 1 + count_even(start + 1, end)
#     else:
#         return count_even(start + 1, end)

# a = int(input("Enter start: "))
# b = int(input("Enter end: "))
# print(f"Count of even numbers: {count_even(a, b)}")



# 6. Find maximum digit in a number using recursion
# def max_digit(n):
#     if n < 10:
#         return n
#     return max(n % 10, max_digit(n // 10))

# num = int(input("Enter number: "))
# print(f"Maximum digit: {max_digit(abs(num))}")



# 7. Print sum of first n Fibonacci values using recursion
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# def sum_fib(n):
#     if n <= 0:
#         return 0
#     return fib(n) + sum_fib(n - 1)

# n = int(input("Enter n: "))
# print(f"Sum of first {n} Fibonacci values: {sum_fib(n)}")



# 8. Check if a number is palindrome using recursion
# def is_palindrome(n, original=None):
#     if original is None:
#         original = n
#     if n < 10:
#         return n == original % 10
#     else:
#         last_digit = n % 10
#         original_last = original % 10
#         if last_digit != original_last:
#             return False
#         return is_palindrome(n // 10, original // 10)

# Alternative simpler approach using string comparison
# def is_palindrome_str(n):
#     s = str(abs(n))
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome_str(int(s[1:-1])) if len(s) > 1 else True

# num = int(input("Enter number: "))
# if is_palindrome_str(num):
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")



# 9. Find LCM of two numbers using recursion
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"LCM of {a} and {b}: {lcm(a, b)}")



#sum of n natural numbers using recursion
# def sumofnat(n):
#     if n==0:
#         return 0
#     return n +sumofnat(n-1)
# n=int(input())
# print(sumofnat(n))


#sum of digits in a given number without using extra varaible using recursion
# def sumofdigit(n):
#     if n==0:
#         return 0
#     return n%10 +sumofdigit(n//10)
# n=int(input())
# print(sumofdigit(n))


#given number is even or not using recursion
# def iseven(n):
#     if n==0:
#         return True
#     elif n==1:
#         return False
#     else:
#         return iseven(n-2)
# n=int(input())
# print(iseven(n))


#nth fibonacci using recuresion
# def nfib(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return nfib(n-1)+nfib(n-2)
# n=int(input())
# print(nfib(n))


#find a target element in a given list by using binary searchj using recursion
def bin(arr,low,high,target):
    if low >high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return bin(arr,low,mid-1,target)
    else:
        return bin(arr,mid+1,high,target)


l=list(map(int,input().split()))
t=int(input())
result=bin(l,0,len(l)-1,t)
print(result)