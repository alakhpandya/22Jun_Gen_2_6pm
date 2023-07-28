from employee import Employee

class SalesExecutive(Employee):
    department = "sales & marketing"
    department_code = "S"
    target = 200000
    
    def __init__(self, name, age, gender, area):
        super().__init__(name, age, gender)
        self.area = area

    def showInfo(self):
        super().showInfo()
        print("Target:", self.target)
        print("Area:", self.area)
        print(f"---------------------------------------------------------")
