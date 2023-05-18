import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def Factorial(x):
    return math.factorial(x) 

def log(x, y):
    return math.log(x,y)

def Root(x):
    return math.sqrt(x)

def Power(x, y):
    return x ** y

def Reminder(x, y):
    return x % y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def decimal_to_binary(num):
    return bin(num).replace("0b", "")

def binary_to_decimal(num):

    return int(num, 2)

def decimal_to_hexadecimal(num):
    return hex(num).replace("0x", "")

def hexadecimal_to_decimal(num):
    return int(num, 16)

print("Calculator")
print("-----------")

Exit ="N"
while (Exit == "N") or (Exit == "n"):
    # Code block to be executed


    print("Select mode:")
    print("1. Standard Calculator")
    print("2. Programmer Calculator")

    mode = input("Enter your choice (1-2): ")

    if mode == '1':
        print("Standard Calculator")
        print("-------------------")

        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Factorial")
        print("6. log")
        print("7. Root")
        print("8. Power")
        print("9. Remainder")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", add(num1, num2))
        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            num1 =float( input("Enter the first number: "))
            num2 =float( input("Enter the second number: "))
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", divide(num1, num2))
        elif choice == '5':
            num1 = int(input("Enter the first number: "))
            print("Result:", Factorial(num1))
        elif choice == '6':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", log(num1, num2))
        elif choice == '7':
            num1 =float( input("Enter the first number: "))
            print("Result:", Root(num1))
        elif choice == '8':
            num1 =float( input("Enter the first number: "))
            num2 =float( input("Enter the second number: "))
            print("Result:", Power(num1, num2))
        elif choice == '9':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", Reminder(num1, num2))
        else:
            print("Invalid input")

    elif mode == '2':
        print("Programmer Calculator")
        print("---------------------")

        print("Select conversion:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Decimal to Hexadecimal")
        print("4. Hexadecimal to Decimal")

        choice = input("Enter your choice (1-4): ")
        num = int(input("Enter a number: "))





        if choice == '1':
            print("Binary:", decimal_to_binary(num))
        elif choice == '2':
            num=str(num)
            print("Decimal:", binary_to_decimal(num))
        elif choice == '3':
            print("Hexadecimal:", decimal_to_hexadecimal(num))
        elif choice == '4':
            num=str(num)
            print("Decimal:", hexadecimal_to_decimal(num))
        else:
            print("Invalid input")

    else:
        print("Invalid input")

    Exit=str(input("Do you want to Exit : "))
