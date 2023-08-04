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

    def generateId(self):
        self.date_of_joining = datetime.today()
        self.id = str(self.date_of_joining.year) + str(self.date_of_joining.month).zfill(2) + self.department_code + str(len(Employee.all_eployees) + 101)

    def showInfo(self):
        print(f"---------------- Info of {self.name} ----------------")
        print("ID:", self.id)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Department:", self.department)
        print("Date of joining:", self.date_of_joining)
    
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
        Employee.authenticate_other(id, pwd)