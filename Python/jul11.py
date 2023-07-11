class Car:
    seats = 5
    allCars = []

    def __init__(self, model, fuel, price):
        self.model = model
        self.fuel = fuel
        self.price = price
        Car.allCars.append(self)

    # method
    def displayInfo(self):
        print(f"------------- Info of {self.model} -------------")
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        print()


c1 = Car("Audi A8", "Petrol", 20000000)
# c1.displayInfo()
# Car.allCars.append(c1)

c2 = Car("Toyota Innova", "Diesel", 4000000)
c2.seats = 7
# c2.displayInfo()

c3 = Car("Scorpio", "Diesel", 2000000)
c3.seats = 7
# c3.displayInfo()

while True:
    print("Press:")
    print("1 to add new car")
    print("2 to view details of a car")
    print("3 to change details of a car")
    print("4 to delete a car")
    print("9 to exit")
    op = int(input())

    if op == 1:
        pass

    elif op == 2:
        """
        print("Sr nos of all the cars in stock:)
        SrNo    Model Name
        0       Audi A8
        1       Toyota Innova
        2       Scorpio
        """
        c = int(input("\tEnter sr no: "))
        Car.allCars[c].displayInfo()

    elif op == 3:
        pass

    elif op == 4:
        pass

    elif op == 9:
        break

    else:
        print("Invalid operation, please try again...")

