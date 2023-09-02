

# Quadratic Eqn: ax^2 + bx + c = 0
"""
sqrt(b^2 - 4ac) < 0 -> No real roots
sqrt(b^2 - 4ac) == 0 -> 1 root
sqrt(b^2 - 4ac) > 0 -> 2 different roots
"""
class SolveQuadratic():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __enter__(self):
        self.delta = self.b**2 - 4*self.a*self.c
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del self.delta

# e1 = SolveQuadratic(2, 3, 4)    # 2x^2 + 3x + 4
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
with SolveQuadratic(a, b, c) as e1:
    if e1.delta < 0:
        print("Sorry, no roots exist.")
    elif e1.delta == 0:
        root = (-e1.b + e1.delta**0.5)/(2 * e1.a)
        print("Root =", root)
    else:
        r1 = (-e1.b + e1.delta**0.5)/(2 * e1.a)
        r2 = (-e1.b - e1.delta**0.5)/(2 * e1.a)
        print(f"""Root-1 = {r1}
Root-2 = {r2}""")

print(e1.delta)
print(e1.a)
print("----------End of the program-----------")

# Practice Examples:
"""
Q1. Frequency of Digit

Problem Description
Given a number A and a digit B. Find the frequency of digit B in the number A.

Return the frequency of digit B.

Problem Constraints
1 <= A <= 109
0 <= B <= 9

Input Format
The first argument is the integer number A.
The second argument will be digit B.

Output Format
Return an integer which denotes the frequency of digit B in A.

Example Input
Input 1:
A = 1213
B = 1

Example Output
Output 1:
2

Example Explanation
Explanation 1:
Frequency of 1 in 1213 is 2


Input 2:
A = 99809
B = 9

Example Output
Output 2:
3

Example Explanation
Explanation 2:
Frequency of 9 in 99809 is 3

---------------------------------------------------------------------------------

Q2. Decimal to Any Base

Problem Description
Given a decimal number A and a base B, convert it into its equivalent number in base B.


Problem Constraints
0 <= A <= 512
2 <= B <= 10


Input Format
The first argument will be decimal number A.
The second argument will be base B.


Output Format
Return the conversion of A in base B.


Example Input
Input 1:
A = 4
B = 3
Input 2:
A = 4
B = 2 


Example Output
Output 1:
11
Output 2:
100


Example Explanation
Explanation 1:
Decimal number 4 in base 3 is 11.
Explanation 2:
Decimal number 4 in base 2 is 100. 

---------------------------------------------------------------------------------

Q3. Any Base to Decimal

Write a program that does exactly opposite to the Q2. That is, converts a given number and base, converts it to the corresponding decimal number.

---------------------------------------------------------------------------------

Q4. Any Base Addition

Problem Description
Given an integer A, and two integers B and C in base A.
Perform the addition of B and C in base A and return the result in base A.

Problem Constraints
2 <= A <= 10
0 <= B, C <= 256 (in decimal system)


Input Format
The first argument is an integer A, which is the base of the other two numbers.
The second argument is the first number B in base A.
The third argument is the second number C in base A.


Output Format
Return the addition of B and C in base A.


Example Input
Input:
A = 3
B = 11
C = 10


Example Output
Output:
21


Example Explanation
11 is the base 3 representation of decimal number 4.
10 is the base 3 representation of decimal number 3.
And sum of 3 and 4 in decimal representation is 7, which is
21 in base 3 representation.

---------------------------------------------------------------------------------

Q5. Any Base Multiplication

Problem Description
Given an integer A, and two integers B and C in base A.
Perform the multiplication of B and C in base A and return the result.

Note - Input is given such that the multiplication will always lie in the integer range.


Problem Constraints
2 <= A <= 10
0 <= B, C <= 256 (in decimal system)


Input Format
The first argument is an integer A, which is the base of the other two numbers.
The second argument is the first number B in base A.
The third argument is the second number C in base A.


Output Format
Return the multiplication of B and C in base A.


Example Input
Input:
A = 3
B = 11
C = 10


Example Output
Output:
110


Example Explanation
11 is the base 3 representation of decimal number 4.
10 is the base 3 representation of decimal number 3.
And multiplication of 3 and 4 in decimal representation is 12, which is
110 in base 3 representation.

"""