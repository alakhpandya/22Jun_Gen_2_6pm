from employee import Employee

class Admin(Employee):
    department = "admin"
    department_code = "A"

    def showInfo(self):
        super().showInfo()
        print(f"---------------------------------------------------------")
