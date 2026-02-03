class Circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(5)

print("Area of the Circle : " , c1.area())
print("Perimeter of the Circle : " , c1.perimeter())