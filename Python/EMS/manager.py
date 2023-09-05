from employee import Employee

class Manager(Employee):
    department = "management"
    department_code = "M"
    education = "MBA"

    def showInfo(self):
        super().showInfo()
        print("Education:", self.education)
        print(f"---------------------------------------------------------")

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender) 