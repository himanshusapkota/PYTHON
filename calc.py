num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
        print("The sum is:", num1 + num2)
elif operation == '-':
        print("The difference is:", num1 - num2)
elif operation == '*':
        print("The product is:", num1 * num2)
elif operation == '/':
        if num2 != 0:
            print("The quotient is:", num1 / num2)
else:
            print("Error: Division by zero is not allowed.")
