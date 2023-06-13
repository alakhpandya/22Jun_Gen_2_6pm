def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def average(*args):
    return sum(args)/len(args)

def absoluteSum(a, b):
    return abs(a) + abs(b)

def palindrome(s):
    s = s.lower()
    return s == s[ : : -1]

# x = int(input())
# y = int(input())
# print(factorial(6))
# print(average(5, 8, 10, 13))
# print(absoluteSum(x, y))