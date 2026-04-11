import math

class SmartCalculator:

    def __init__(self):
        pass

    def add(self , a , b):
        return a + b

    def substract(self , a , b):
        return a - b

    def multiply(self , a , b):
        return a * b

    def divide(self , a , b):
        if b==0:
            return "Error: Division by zero"
        return a / b

    def power(self , a , b):
        return a ** b

    def square(self , a):
        return math.sqrt(a)

    def sin(self , a):
        return math.sin(a)

    def cos(self , a):
        return math.cos(a)

    def tan(self , a):
        return math.tan(a)

    def log(self , a):
        return math.log10(a)

    def exp(self , a):
        return math.exp(a)

    def factorial(self , a):
        return math.factorial(a)

    def evaluate(self , expression):
        try:
            return eval(expression)
        except Exception as e:
            return f"Error: {str(e)}"


