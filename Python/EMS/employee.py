class Employee:
    all_eployees = []

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Employee.all_eployees.append(self)

    def showInfo(self):
        print(f"---------------- Info of {self.name} ----------------")
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Department:", self.department)

    def authenticate_admin(id, pwd):
        if "A" not in id:
            return False
        index = int(id[-3 : ]) - 101
        emp = Employee.all_eployees[index]
        if emp.id == id and emp.pwd == pwd:
            return True
        return False
    
    def authenticate_other(id, pwd):
        pass