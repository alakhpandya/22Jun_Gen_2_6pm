"""
Write a Python recursive function to print nth term of Fibonacci Sequence where 'n' tobe taken from user.
Fibonacci Sequence:
1, 1, 2, 3, 5.....

1st term = 1
2nd term = 1
nth term = (n - 1)th term + (n - 2)th term
"""
# Memoization - Explicit
"""
n = int(input("Enter n : "))
cache_memory = {}
def findFibo(n):
    if n in cache_memory:
        return cache_memory[n]
    if n==1 or n==2:
        cache_memory[n] = 1
        return 1
    else:
        term = findFibo(n-1)+findFibo(n-2)
        cache_memory[n] = term
        return term

for i in range(1,n+1):
    print(f"{i} = {findFibo(i)}")
print(cache_memory)
"""
"""
cache_memory = {}
# key: "Manish"
# value: 154
cache_memory["Manish"] = 154
cache_memory["Urmi"] = 147
cache_memory["Aarav"] = 105
# print(cache_memory)
key = input("Key: ")
if key in cache_memory:
    print("Yes")
"""

# Memoization - Implicit
"""
from functools import lru_cache

# Decorator = Wrapper Function

# @lru_cache(maxsize=1000)
@lru_cache(maxsize=4)
def findFibo(n):
    if n==1 or n==2:
        return 1
    else:
        return findFibo(n-1)+findFibo(n-2)

n = int(input("Enter n : "))
for i in range(1,n+1):
    print(f"{i} = {findFibo(i)}")
"""

# Organizing our code in modules & packages

N = int(input())
if N % 3 == 0:
    print("Fizz", end="")
if N % 5 == 0:
    print("Buzz")