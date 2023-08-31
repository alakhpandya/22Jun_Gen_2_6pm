from datetime import datetime

class Employee:
    all_eployees = []

    def __init__(self, name: str, age: int, gender: str):
        assert isinstance(name, str), "Employee name must be a string."
        self.name = name

        assert isinstance(age, int), "Age must be integer."
        assert age >= 18, "We don't hire employees under 18."
        self.age = age

        assert isinstance(gender, str), "Employee gender must be a string."
        self.gender = gender
        
        self.generateId()
        Employee.all_eployees.append(self)

        # self.username = self.name[:4] + self.id[:4]
        self.pwd = self.name[:4] + "123"

        self.is_active = True

    def generateId(self):
        self.date_of_joining = datetime.today()
        self.id = str(self.date_of_joining.year) + str(self.date_of_joining.month).zfill(2) + self.department_code + str(len(Employee.all_eployees) + 101)

    @staticmethod
    def showAllEmployees():
        print("SrNo\t" + "Emp.ID\tName\tDepartment".expandtabs(13))
        i = 1
        for emp in Employee.all_eployees:
            if emp.is_active:
                print(f"{i}\t" + f"{emp.id}\t{emp.name}\t{emp.department}".expandtabs(13))
                i += 1

    @staticmethod
    def choseEmployee():
        Employee.showAllEmployees()
        empId = input("Enter the id: ")
        index = int(empId[-3: ]) - 101
        return index

    def showInfo(self):
        print(f"---------------- Info of {self.name} ----------------")
        print("ID:", self.id)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Department:", self.department)
        print("Date of joining:", self.date_of_joining)

    def updateInfo(self):
        print("Enter new details:")
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.gender = input("Gender: ")
        year = int(input("Joining Year: "))
        month = int(input("Month: "))
        date = int(input("Date: "))
        self.date_of_joining = datetime(year=year, month=month, day=date)
        self.pwd = input("Password: ")

    def removeEmployee(self):
        self.is_active = False

    # @staticmethod
    # def removeEmployee(index):
    #     Employee.all_eployees.pop(index)
    #     Employee.all_eployees.insert(index, None)

    @staticmethod
    def addEmployee():
        print("Enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return name, age, gender
    
    def authenticate_other(id, pwd):
        index = int(id[-3 : ]) - 101
        emp = Employee.all_eployees[index]
        if emp.id == id and emp.pwd == pwd:
            department_code = id[-4]
            return department_code
        return False
    
    def authenticate_admin(id, pwd):
        if "A" not in id:
            return False
        return Employee.authenticate_other(id, pwd)