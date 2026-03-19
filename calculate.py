def calculate(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."


while True:
    try:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        symbol = input("Enter the symbol for the operation (+, -, *, /): ")
        break
    except ValueError:
        print("Invalid input. Please enter valid integers.")

result = calculate(n1, n2, symbol)
print("The result is:", result)