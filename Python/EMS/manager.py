from employee import Employee

class Manager(Employee):
    department = "management"
    department_code = "M"
    education = "MBA"

    def showInfo(self):
        super().showInfo()
        print("Education:", self.education)
        print(f"---------------------------------------------------------")
