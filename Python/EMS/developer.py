from employee import Employee

class Developer(Employee):
    department = "IT"
    department_code = "D"

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)
 