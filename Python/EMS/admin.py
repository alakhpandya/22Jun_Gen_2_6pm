from employee import Employee

class Admin(Employee):
    department = "admin"
    department_code = "A"

    def showInfo(self):
        super().showInfo()
        print(f"---------------------------------------------------------")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)