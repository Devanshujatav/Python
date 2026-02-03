class Employee():
    company = "TechCorp"
    def __init__(self , name , age , position):
        self.name = name
        self.age = age
        self.position = position

    def display(self):
        print(f"{self.name} is a {self.position} at {Employee.company}")

    @classmethod
    def update_company(cls , new_company):
        cls.company = new_company

    @staticmethod
    def welcome_message():
        print("Welcome to the Employee Management System")


Employee.welcome_message()

emp1 = Employee("Alice" , "30" , "Developer")
emp2 = Employee("Bob" , "35" , "Manager")

emp1.display()
emp2.display()

Employee.update_company("TCS")
emp2.display()