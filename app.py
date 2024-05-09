import math

def scientific_calculator():
    print("Welcome to the Advanced Scientific Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Trigonometric functions (sin, cos, tan)")
    print("9. Exit")

    while True:
        choice = input("Enter operation number or '9' to exit: ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

        if choice == '1':
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            result = num1 * num2
            print("Result:", result)
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                result = num1 / num2
                print("Result:", result)
        elif choice == '5':
            result = num1 ** num2
            print("Result:", result)
        elif choice == '6':
            result = math.sqrt(num1)
            print("Square Root of", num1, "is:", result)
        elif choice == '7':
            base = float(input("Enter the base (default is 10): ") or '10')
            result = math.log(num1, base)
            print("Logarithm of", num1, "to the base", base, "is:", result)
        elif choice == '8':
            angle = float(input("Enter the angle in degrees: "))
            radian = math.radians(angle)
            print("sin(", angle, ") =", math.sin(radian))
            print("cos(", angle, ") =", math.cos(radian))
            print("tan(", angle, ") =", math.tan(radian))
        else:
            print("Invalid operation number! Please enter a valid operation.")

if __name__ == "__main__":
    scientific_calculator()
