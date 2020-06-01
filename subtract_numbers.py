"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    The code in the main function calls the function subtract_two_numbers which performs the computaion on the numbers the user inputs.
    """
    print("The result is:" + str(subtact_two_numbers()))


"""This function asks user to input two numbers and then subtracts the second number from the first"""
def subtact_two_numbers():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    """num3 stores the result of the subtraction between num1 and num2"""
    num3 = num1 - num2
    """return returns the value of num3 to the main function"""
    return num3

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
