from employee import Employee

class Peon(Employee):
    department = "house keeping"
    department_code = "P"

    def showInfo(self):
        super().showInfo()
        print(f"---------------------------------------------------------")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender) 