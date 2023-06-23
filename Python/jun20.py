# Random module
import random

# print(dir(random))
"""

# print(random.random())    # will return a random float in the interval [0, 1)
# Write a program to generate 20 random floats/integers in the interval [25, 40)

for i in range(20):
    print(int(random.random()*15 + 25))


for i in range(20):
    print(random.uniform(25, 40))
    # print(random.randrange(25, 40))
    # print(random.randint(25, 40))
"""

# Write a program that generate 100000 random numbers between 1 to 100 (including both). Count how many of them are in intervals [1, 25], [26, 50], [51, 75], [76, 100]. Display their counts.
"""
    Cherish Karmant Meet    Vinit
c1 = 25251  24492   25327   25324
c2 = 25450  24854   25276   25377
c3 = 25169  24874   25253   24941
c4 = 24130  25780   24144   24358
"""
# Normal Distribution
"""
for i in range(20):
    print(random.normalvariate(30, 5))
    # print(random.normalvariate(30, 1))
"""

# user: rock, paper, scissors
# computer: randomly produce one of rock, paper, scissors
# You won! or Computer won!
# user score += 1 if user wins
# computer score += 1 if computer wins
# do this 10 times. Print final score and the winner.

# Monte Carlo Problem