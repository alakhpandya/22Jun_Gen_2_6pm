from datetime import datetime
"""
temp = "July 22, 2019 at 2.43pm"
c2 = datetime.strptime(temp, "%B %d, %Y at %I.%M%p")
print(c2)
"""

import time
from functools import lru_cache
# print(dir(time))
# print(time.time())
# epoch: 1st January, 1970

"""
@lru_cache()
def findFibo(n):
    if n==1 or n==2:
        return 1
    else:
        return findFibo(n-1)+findFibo(n-2)
"""
"""
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
"""
"""
# n = int(input("Enter n : "))
avg_time = 0
for x in range(50):
    t1 = time.time()
    n = 100000
    for i in range(1,n+1):
        # print(f"{i} = {findFibo(i)}")
        findFibo(i)

    t2 = time.time()
    avg_time += (t2 - t1)

print("\n\n", round(avg_time/50, 4))
"""

# Using time module, calculate the time taken to create a list (containing integers from 1 to 10000 computed using list comprehension) 10,000 times. Also calculate the time to create same set 10,000 times and conclude whether it is faster to create list or set.
"""
t1 = time.time()
for x in range(10000):
    l = [i for i in range(1, 10001)]
t2 = time.time()
lt = t2-t1

t3 = time.time()
for x in range(10000):
    s = {i for i in range(1, 10001)}
t4 = time.time()
st = t4-t3

print("list time:", lt)
print("set time:", st)
"""

# timeit module
"""
from timeit import timeit

lt = timeit("l = [i for i in range(1, 10001)]", number=10000)
st = timeit("s = {i for i in range(1, 10001)}", number=10000)
print("list time:", lt)
print("set time:", st)
"""

# OOP in Python

# POP: Procedure Oriented Programming

# Car showroom:
"""
5 cars * 10 = 50 different cars
each car: bhp, airbags, transmission, fuel, price, mileage, color, seating capacity, sunroof, stock
add a new car
edit a particular car
delete an existing car
show details of a car

car = [
    []
]

c1 = {bhp:150, airbags:4, transmission:auto, fuel:Petrol, price:1800000, mileage:14, color:Black, seating capacity:4, sunroof:True, stock:10}

car class:

"""

class Car:
    seats = 2       # class variable


Car.seats = 7
c1 = Car()
# object varables:
c1.model = "Audi R8"
c1.fuel = "Petrol"
c1.price = 50000000

print("Model:", c1.model)
print("Fuel:", c1.fuel)
print("Price:", c1.price)
print("Seats:", c1.seats)
print(c1.__dict__)
print()


c3 = Car()
c3.model = "Nexon"
c3.fuel = "Electric"
c3.price = 1800000
c3.seats = 5

print("Model:", c3.model)
print("Fuel:", c3.fuel)
print("Price:", c3.price)
print("Seats:", c3.seats)
print(c3.__dict__)
print()


c2 = Car()
c2.model = "Toyota Supra"
c2.fuel = "Diesel"
c2.price = 2000000

print("Model:", c2.model)
print("Fuel:", c2.fuel)
print("Price:", c2.price)
print("Seats:", c2.seats)
print(c2.__dict__)
print()

