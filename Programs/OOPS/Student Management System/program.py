class Student:
    def __init__(self , name , marks1 , marks2 , marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1+self.marks2+self.marks3)/3
        return avg


student1 = Student("Amit" , 99 , 98 , 97)
# print(student1.average())
avg = student1.average()
print("The Average of" , student1.name , "is", avg)
