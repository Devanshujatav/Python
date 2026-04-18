from random import choice

from calculator import SmartCalculator

def run():
    calc = SmartCalculator()

    while True:
        print("\n SMART CALCULATOR \n")
        print("1. Basic Operations")
        print("2. Scientific Functions")
        print("3. Evaluate Expressions")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("1. Add   2. Subtract  3. Multiply  4. Divide")
            op = input("Enter operation : ")

            if op == "1": print(calc.add(a, b))
            elif op == "2": print(calc.substract(a, b))
            elif op == "3": print(calc.multiply(a, b))
            elif op == "4": print(calc.divide(a, b))

        elif choice == "2":
            print(
                "1. sqrt 2. sin 3. cos 4. tan 5. log 6. factorial"
            )

            op = input("Enter operation : ")
            a = float(input("Enter the number: "))

            if op == "1": print(calc.square(a))
            elif op == "2": print(calc.sin(a))
            elif op == "3": print(calc.cos(a))
            elif op == "4": print(calc.tan(a))
            elif op == "5": print(calc.log(a))
            elif op == "6": print(calc.factorial(a))

        elif choice == "3":
            expr = input("Enter the expression : ")
            print(calc.evaluate(expr))

        elif choice == "4":
            print("Thank you for using Smart Calculator")
            break

        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    run()