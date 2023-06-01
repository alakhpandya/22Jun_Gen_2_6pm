# Recursion:
"""
if clause: non-recursive step
else clause: recursive step
"""
# Example:
# factorial function:
"""
recursive step: 
n! = n * (n - 1)!
# 25! = 25 * 24!
# 11! = 11 * 10!

Non-recursive step:
0! = 1
"""
"""
def recFact(n):
    if n == 0:
        return 1
    else:
        return n * recFact(n-1)
    
a = int(input())
print(recFact(a))
"""
# HW:

# Write a recursive Python function to find nth term of an Arithmetic Progression whose first term is 'a' and common difference is 'd'. In the main program, ask 'a', 'n' & 'd' from the user, pass it into the function and print the answer returned by the function.

# Arithmetic Progression with a = 4 & d = 3
# ap: 4, 7, 10, 13, 16, 19, 22

# 7th term = 6th term + d
"""
Recursive Step:
nth term = (n-1)th term + d

Non-recursive Step:
1st term = a
"""

# Write a recursive Python function to find nth term of a Geometric Progression whose first term is 'a' and common ratio is 'r'. In the main program, ask 'a', 'n' & 'r' from the user, pass it into the function and print the answer returned by the function.

# Geometric Progression with a = 4 & r = 3
# gp: 4, 12, 36, 108, 324.....

# 7th term = 6th term * r
"""
Recursive Step:
nth term = (n-1)th term * r

Non-recursive Step:
1st term = a
"""



