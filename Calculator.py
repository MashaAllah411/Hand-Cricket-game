class Calculator:
    def __init__(self):
        self.number1 = int(input("Enter the first number: "))
        self.number2 = int(input("Enter the second number: "))
        self.operation = input("Enter an operation (+, -, *, /): ")
        
    def operations(self):
        if self.operation == "*":
            return self.number1 * self.number2
        elif self.operation == "-":
            return self.number1 - self.number2
        elif self.operation == "+":
            return self.number1 + self.number2
        elif self.operation == "/":
            try:
                return self.number1 / self.number2
            except ZeroDivisionError:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

# Running the calculator
calc = Calculator()
result = calc.operations()
print("Result:", result)
