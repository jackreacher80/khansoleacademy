"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    The main function calls four functions addition_console(), subtraction_console(),multiplication_console() and division_console()
    that tests the user on his knowledge of addition, subtraction, multiplication and division.
    """

    addition_console()
    print("Congratulations!  You mastered addition")
    subtraction_console()
    print("Congratulations!  You mastered subtraction")
    multiplication_console()
    print("Congratulations!  You mastered multiplication")
    division_console()
    print("Congratulations!  You mastered division")


"""This function asks the user an addition problem and gives him feedback on his results. The user must be correct 3 times for the system to move
move from addition to subtraction to multiplication to division"""
def addition_console():
    correct_answer_count = 0
    """pre-condition-correct_answer_count is not equal to 3
       post-condition-correct_answer_count is equal to 3 and loop terminates
    """
    while correct_answer_count != 3:
        """num1 and num2 are numbers generated randomly. num3 stores the result of the addition of num1 and num2"""
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num3 = num1 + num2
        print("What is " + str(num1) + "+ " + str(num2) + "? ")
        """user is asked for his input to the addition problem"""
        num4 = float(input("your answer: "))
        """User input is compared to the actual result and it is shown to him"""
        if num4 == num3:
            correct_answer_count = correct_answer_count + 1
            print("You've gotten  " + str(correct_answer_count) + " correct in a row ")
        else:
            print("Incorrect. The expected answer is  " + str(num3))

"""This function asks the user an subtraction problem and gives him feedback on his results. The user must be correct 3 times for the system to move
move from addition to subtraction to multiplication to division"""
def subtraction_console():
    correct_answer_count = 0
    """pre-condition-correct_answer_count is not equal to 3
       post-condition-correct_answer_count is equal to 3 and loop terminates
        """
    while correct_answer_count != 3:
        """num1 and num2 are numbers generated randomly. num3 stores the result of the subtraction of num1 and num2"""
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num3 = num1 - num2
        print("What is " + str(num1) + "- " + str(num2) + "? ")
        """user is asked for his input to the subtraction problem"""
        num4 = float(input("your answer: "))
        """User input is compared to the actual result and it is shown to him"""
        if num4 == num3:
            correct_answer_count = correct_answer_count + 1
            print("You've gotten  " + str(correct_answer_count) + " correct in a row ")
        else:
            print("Incorrect. The expected answer is  " + str(num3))

"""This function asks the user a multiplication problem and gives him feedback on his results 
The user must be correct 3 times for the system to move from addition to subtraction to multiplication to division
"""
def multiplication_console():
        correct_answer_count = 0
        """pre-condition-correct_answer_count is not equal to 3
           post-condition-correct_answer_count is equal to 3 and loop terminates
        """
        while correct_answer_count != 3:
            """num1 and num2 are numbers generated randomly. num3 stores the result of the multiplication of num1 and num2"""
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            num3 = num1 * num2
            print("What is " + str(num1) + "*" + str(num2) + "? ")
            """user is asked for his input to the multiplication problem"""
            num4 = float(input("your answer: "))
            """User input is compared to the actual result and it is shown to him"""
            if num4 == num3:
                correct_answer_count = correct_answer_count + 1
                print("You've gotten  " + str(correct_answer_count) + " correct in a row ")
            else:
                print("Incorrect. The expected answer is  " + str(num3))


"""This function asks the user a division problem and gives him feedback on his results 
The user must be correct 3 times for the system to move from addition to subtraction to multiplication to division
"""
def division_console():
    correct_answer_count = 0
    """pre-condition-correct_answer_count is not equal to 3
       post-condition-correct_answer_count is equal to 3 and loop terminates
    """
    while correct_answer_count != 3:
        """num1 and num2 are numbers generated randomly. num3 stores the result of the division of num1 and num2"""
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num3 = num1 / num2
        print("What is " + str(num1) + "/" + str(num2) + "? ")
        """user is asked for his input to the multiplication problem"""
        print("Please enter a value with 17 digits after the decimal")
        num4 = float(input("your answer: "))
        """User input is compared to the actual result and it is shown to him"""
        if num4 == num3:
            correct_answer_count = correct_answer_count + 1
            print("You've gotten  " + str(correct_answer_count) + " correct in a row ")
        else:
            print("Incorrect. The expected answer is  " + str(num3))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
