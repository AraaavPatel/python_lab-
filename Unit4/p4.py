def calculate(a, b, op):
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    else:
        print("Invalid operator")

# Input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/): ")

calculate(x, y, operator)