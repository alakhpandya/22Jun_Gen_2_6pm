"""
class Car:
    allCars = ["i10", "i20", "creta", "hector", "sonet"]

    @staticmethod
    def printStock():
        print("Printing all stock")
        c = int(input("Index no: "))    # 2
        return c
    
# print(Car.allCars)
# c = Car.printStock()
# Car.allCars.pop(c)
# print(Car.allCars)

a = 5
b = 3.8
c = "Car"
# print(isinstance(a, int))
# print(isinstance(b, int))
# print(isinstance(c, int))
print(isinstance(c, str))
"""

# 4 Pillars of OOP: Inheritance, Abstraction, Polymorphism, Encapsulation

# Inheritance: Single level/Single/Simple inheritance, Multi-level Inheritance, Hierarchical Inheritance, Hybrid Inheritance, Multiple Inheritance
"""
class Car:
    seats = 5
    allCars = []

    def __init__(self, model:str, fuel:str, price:float):
        assert isinstance(model, str), "Model name should be string only."
        self.model = model

        assert isinstance(fuel, str), "Fuel type should be string only."
        self.fuel = fuel

        assert isinstance(price, int), "Price should be integer only."
        self.price = price
        Car.allCars.append(self)


    def displayInfo(self):
        print(f"------------- Info of {self.model} -------------")
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        print()


class Maruti(Car):
    make = "Maruti"
    # seats = 4
    def displayInfo(self):
        print(f"------------- Info of {self.model} -------------")
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        print("Make:", self.make)
        print()

class Ertiga(Maruti):
    seats = 7


class Tata(Car):
    make = "Tata"

class Nexon(Tata):
    pass

m1 = Maruti("Baleno", "Petrol", 800000)
# print(m1.seats)
# m1.displayInfo()

e1 = Ertiga("ZDI", "Diesel", 1200000)
e1.displayInfo()

# MRO: Method Resolution Order - Object Vaiable -> Class variable of Own Class -> Class variable of parent classes

e2 = Ertiga("6seater ZXI", "Petrol", 1100000)
e2.seats = 6
# e2.displayInfo()
"""
"""
class Father:
    profession = "Business"

class Mother:
    vehicle = "Mercedes AMG"
    profession = "Doctor"

# class Child(Father, Mother):
class Child(Mother, Father):
    vehicle = "Bicycle"

c1 = Child()
print(c1.profession)
print(c1.vehicle)
"""

class A():
    v1 = 10

class B():
    v1 = 11
    v2 = 20

class C(A):
    pass

class D(B):
    pass

class E(C, D):
    pass

c1 = C()
print(c1.v1)

d1 = D()
print(d1.v1)

e1 = E()
print(e1.v1)