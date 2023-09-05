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
import json

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

def writeIntoDatabse():
    with open('database.csv', 'w') as f:
        for employee in Employee.all_eployees:
            f.write(str(employee.__dict__))
            f.write("\n")

def strToDict(data):
    data = data[ : -2]
    # This line is creating error:
    data = data[:47] + data[117:]
    # Hint: instead of removing like this, use occurance of "," and remove based on that
    data = data.split(",")
    
    obj_dict = {}
    for pair in data:
        key, value = pair.split(":")
        key = key[1:]
        value = value[1:]
        obj_dict[key] = value
    return obj_dict

def readFromDatabase():
    with open('database.csv', 'r') as f:
        data = f.readlines()
        for i in range(len(data)):
            obj = strToDict(data[i])
            # print(obj)
            name = obj["'name'"][1:-1]
            age = int(obj["'age'"])
            gender = obj["'gender'"][1 : -1]
            id = obj["'id'"][1 : -1]
            pwd = obj["'pwd'"][1 : -1]
            is_active = bool(obj["'is_active'"])
            department_code = id[6]
            if department_code == 'A':
                emp = Admin(name, age, gender)
            elif department_code == 'D':
                emp = Developer(name, age, gender)
            elif department_code == 'M':
                emp = Manager(name, age, gender)
            elif department_code == 'P':
                emp = Peon(name, age, gender)
            elif department_code == 'S':
                area = obj["'area'"][1 : -1]
                emp = SalesExecutive(name, age, gender, area)
            emp.id = id
            emp.pwd = pwd
            emp.is_active = is_active

readFromDatabase()
# login_type = login()
login_type = "A"
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
            print("Enter:")
            print("1 to add an Admin")
            print("2 to add a Sales Executive")
            print("3 to add a developer")
            print("4 to add a manager")
            print("5 to add a peon")
            emp_type = int(input())
            class_selection = {
                1 : Admin.addEmployee,
                2 : SalesExecutive.addEmployee,
                3 : Developer.addEmployee,
                4 : Manager.addEmployee,
                5 : Peon.addEmployee
            }
            class_selection[emp_type]()

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
            writeIntoDatabse()
            break

        else:
            print("Invalid input, try again...")