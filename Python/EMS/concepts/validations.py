x = 6
y = "10"

class Car():
    pass

class Sedan(Car):
    pass

c1 = Car()
s1 = Sedan()
# print(isinstance(c1, Car))
# print(isinstance(c1, Sedan))
# print(isinstance(s1, Sedan))
# print(isinstance(s1, Car))

# print(isinstance(y, str))
# print(isinstance(x, float))

assert x > 5, "value of x should be more than 5"
assert isinstance(y, str), "y must be a string."