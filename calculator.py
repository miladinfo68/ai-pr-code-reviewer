# calculator.py

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raises an error if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")
    print(f"Division: {divide(num1, num2)}")
    
# A simple calculator that performs basic arithmetic operations.
# added sample 1 
# added sample 2

# 2222222
# 3333333
   
 
