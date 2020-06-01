"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    he main function calls the function godel_function() that solves the problem
    """

    num1 = int(input("Please enter the value of n: "))
    godel_function(num1)

"""This function solves the problem mentioned by Hofstadter"""
def godel_function(n):
    """The count variable tracks the count it took for the num1 to become 1"""
    count = 0
    """pre-condition-n is not equal to 1
       post-condition-n is equal to 1 and the loop terminates
    """
    while n != 1:
        """If the number is odd then 3n+1 is computed or if it is even then the number is halved"""
        if n % 2 != 0:
            num2 = (3*n)+1
            print(str(n)+" is odd, so I make 3n+1: "+str(num2))
        else:
            num2 = n/2
            print(str(n)+" is even, so I take half: "+str(num2))
        n = num2
        count = count+1
    print("The process took "+str(count)+" steps to reach 1")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
