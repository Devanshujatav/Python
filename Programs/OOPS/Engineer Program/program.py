class Employee:
    def __init__(self , role , department , salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role : ", self.role)
        print("Department : ", self.department)
        print("Salary : ", self.salary)

class Engineer(Employee):
    def showDetails(self):
        super().showDetails()
        print("Name : ", self.name)
        print("Age : ", self.age)

    def __init__(self , name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer" , "IT" , "$75000")





engg1 = Engineer("Devanshu Jatav" , "21")

print(engg1.showDetails())




#
# e = Employee("SDE" , "anti missile system development" , 500000)
#
# print(e.showDetails())