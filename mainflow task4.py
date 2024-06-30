#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers. Handles division by zero."""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_number(prompt):
    """Function to get a valid number from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the valid options
        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"The result of {num1} + {num2} is: {add(num1, num2)}")

            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"The result of {num1} / {num2} is: {result}")

            # Ask the user if they want to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input. Please select a valid operation (1/2/3/4).")

    print("Thank you for using the Simple Calculator. Goodbye!")

if __name__ == "__main__":
    main()


# In[ ]:




