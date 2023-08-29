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
import sys

def login():
    while True:
        print("Enter")
        print("1 if you are an admin")
        print("2 if you are an employee")
        print("3 to exit")
        user_type = int(input())
        if user_type == 3:
            return False
        id = input("ID: ")
        pwd = input("Password: ")
        if user_type == 1:
            department_code = Employee.authenticate_admin(id, pwd)
        elif user_type == 2:
            department_code = Employee.authenticate_other(id, pwd)
        else:
            print("Invalid. Please try again.")
        if department_code:
                return department_code

p1 = Peon("Krunal", 23, "Male")  # Peon - 202104P114, alakh123
a1 = Admin("Priyanka", 26, "Female")   # Admin
m1 = Manager("Niti", 25, "Female")
s1 = SalesExecutive("Sandeep", 23, "Male", "Ahmedabad West")
# p1.showInfo()
# a1.showInfo()    
# m1.showInfo()
# s1.showInfo()
# Employee.all_eployees[3].showInfo()

login_type = login()
if not login_type:
    print("Sorry, could not logged you in...")
    sys.exit()
while True:
    if login_type == "A":
        print("Enter:")
        print("1 to add new employee")
        print("2 to see info of an employee")
        print("3 to change info of an employee")
        print("4 to view all employee")
        print("5 to remove an employee")
        
        print("9 to exit")
        action = int(input())

        if action == 1:
            pass

        elif action == 2:
            index = Employee.choseEmployee()
            Employee.all_eployees[index].showInfo()

        elif action == 3:
            index = Employee.choseEmployee()
            Employee.all_eployees[index].updateInfo()

        elif action == 4:
            Employee.showAllEmployees()

        elif action == 5:
            index = Employee.choseEmployee()
            Employee.all_eployees[index].removeEmployee()
            # Employee.removeEmployee(index)

        elif action == 9:
            break

        else:
            print("Invalid input, try again...")