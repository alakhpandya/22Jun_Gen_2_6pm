"""
Employee ID - generate: format: 202201P101, 202202D102, 202207M103
CL: Casual Leave
salary calculation:
    working days vs days worked
    hours puched daily - half day, quarter day, full leave
Increment, Promotion
Incentives

Add employee, edit details, show details, remove employee

Admin
Peon
Manager
Sale Executive
Developer
General Manager
"""
from employee import Employee
from admin import Admin
from developer import Developer
from manager import Manager
from peon import Peon
from salesExecutive import SalesExecutive



p1 = Peon("Krunal", 23, "Male")  # Peon - 202104P114, alakh123
a1 = Admin("Priyanka", 26, "Female")   # Admin
m1 = Manager("Niti", 25, "Female")
s1 = SalesExecutive("Sandeep", 23, "Male", "Ahmedabad West")
# a1.showInfo()    
# m1.showInfo()
# s1.showInfo()
Employee.all_eployees[3].showInfo()


while True:
    print("Enter")
    print("1 if you are an admin")
    print("2 if you are an employee")
    user_type = int(input())
    id = input("ID: ")
    pwd = input("Password: ")
    if user_type == 1:
        authenticate_admin(id, pwd)
    elif user_type == 2:
        authenticate_other(id, pwd)
    else:
        print("Invalid. Please try again.")

"""
while True:
    print("Enter:")
    print("1 to add new employee")
    print("2 to see info of an employee")
    print("3 to change info of an employee")
    print("4 to view all employee")
    print("5 to remove an employee")
    
    print("9 to exit")
    choice = 
"""