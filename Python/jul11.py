class Car:
    seats = 5
    allCars = []

    def __init__(self, model:str, fuel:str, price:float):
        assert isinstance(model, str), "Model name should be string only."
        self.model = model

        assert isinstance(fuel, str), "Fuel type should be string only."
        self.fuel = fuel

        assert isinstance(price, float), "Price should be float only."
        self.price = price
        Car.allCars.append(self)

    # method
    def displayInfo(self):
        print(f"------------- Info of {self.model} -------------")
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        print()

    def updateInfo(self):
        print("\tEnter new info: (press Enter to keep info same)")

        model = input("\tModel: ")
        if model != "": self.model = model

        fuel = input("\tFuel: ")
        if fuel != "": self.fuel = fuel

        price = input("\tPrice: ")
        if price != "": self.price = int(price)

        seats = input("\tSeats: ")
        if seats != "": self.seats = int(seats)

    @staticmethod
    def printStock():
        print("\tSr nos of all the cars in stock: ")
        print("\tSr no.\tModel Name")
        for i in range(len(Car.allCars)):
            print(f"\t{i}\t{Car.allCars[i].model}")
        c = int(input("\tEnter sr no: "))
        return c

    @classmethod
    def addNewCar(cls):
        print("Enter the following details:")
        model = input("Model name: ")
        fuel = input("Fuel type: ")
        price = int(input("Price: "))
        return cls(model, fuel, price)

c1 = Car("Audi A8", "Petrol", 2)
# c1.displayInfo()
# Car.allCars.append(c1)

c2 = Car("Toyota Innova", "Diesel", 4000000)
c2.seats = 7
# c2.displayInfo()

c3 = Car("Scorpio", "Diesel", 2000000)
c3.seats = 7
# c3.displayInfo()

# c4 = Car("911", "Petrol", 5.5)
# c4.seats = 2

while True:
    print("Press:")
    print("1 to add new car")
    print("2 to view details of a car")
    print("3 to change details of a car")
    print("4 to delete a car")
    print("9 to exit")
    op = int(input())

    if op == 1:
        # Maruti.addNewCar()
        # Hyundai.addNewCar()
        Car.addNewCar()

    elif op == 2:
        """
        print("Sr nos of all the cars in stock:)
        SrNo    Model Name
        0       Audi A8
        1       Toyota Innova
        2       Scorpio
        """
        c = Car.printStock()
        Car.allCars[c].displayInfo()

    elif op == 3:
        c = Car.printStock()
        Car.allCars[c].updateInfo()

    elif op == 4:
        c = Car.printStock()
        Car.allCars.pop(c)

    elif op == 9:
        break

    else:
        print("Invalid operation, please try again...")

# Next class: decorators in detail