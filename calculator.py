# 1. Use functions for each operation (+, -, *, /)

def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of two numbers, handling division by zero."""
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2

# Dictionary to map operator symbols to the corresponding function
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# 2. Take user input using input() and 3. Loop until user chooses to exit

def calculator():
    """The main function to run the CLI calculator."""
    print("Welcome to the Python CLI Calculator!")
    
    # Loop continuously until the user decides to exit
    while True:
        print("\n---")
        print("Available Operations: +, -, *, /")
        
        # Get the first number (n1)
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
            
        # Get the operation symbol
        operation_symbol = input("Pick an operation (+, -, *, /): ")

        if operation_symbol not in operations:
            print("Invalid operation symbol. Please choose one of +, -, *, /.")
            continue
            
        # Get the second number (n2)
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Get the function based on the symbol and calculate the result
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        
        # Display the result
        print(f"\n{num1} {operation_symbol} {num2} = {result}")
        
        # Ask if the user wants to continue or exit
        should_continue = input("\nType 'y' to calculate again, or 'n' to exit: ").lower()
        
        if should_continue == 'n':
            print("Goodbye!")
            break

# Run the calculator when the script is executed
if __name__ == "__main__":
    calculator()
