def main():
    while True:
        num1 = float(input("\nEnter the first number: "))
        ope = input("Enter the operation (+, -, *, / or **): ")
        num2 = float(input("Enter the second number: "))
        print(f"Result: {calculator(num1, ope, num2)}")
        choice = int(input("\nDo you want to perform another operation? (1 - yes or 0 - no)" ))
        if choice != 1:
            break
    

def calculator(num1, ope, num2):  
    if ope == "+":
        return num1 + num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            return num1 / num2
    elif ope == "**":
        return pow(num1, num2)
    else:
        return "Invalid operation"


main()