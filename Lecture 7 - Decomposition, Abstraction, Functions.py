# Functions or Procedures are reusable pieces of code.
# Functions are only useful when they are run, "called" or "invoked"
# You write a function once but can run it many times

# Function characteristics;
#   Has a name
#   Has parameters (0 or more)
#   Has a docstring (optional but recommended)
#   Has a body; set of instructions
#   Returns something; keyword return

# <HOW TO WRITE A FUNCTION: is_even example>

def is_even (i):

    """
    :param i: i, a positive int
    :return: True if i is even, otherwise False
    """

    '''if i % 2 == 0:
        return True
    else:
        return False''' #less efficient code

    return i % 2 == 0 # this is a faster way of returning even number as i%2 is a Boolean that evaluates to True/False already


# <QUESTION 1: Div by function>
# define a function that returns True if d divides n evenly

def div_by(n,d):

    """
    n and d are ints > 0
    Returns True if d divides n evenly and False otherwise
    """
    return n % d == 0

print(div_by(8,2))
print(div_by(10,3))
print(div_by(195,13))


# <INSERTING FUNCTIONS IN CODE 1>

print("Numbers between 1 and 10: even or odd")

for i in range(1,10):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")


# <INSERTING FUNCTIONS IN CODE 2>
# suppose we want to add all the odd integers between (and including) a and b
# what is the input (values for a and b)
# what is the output (sum_of_odds)

def sum_odd(a,b):

    sum_of_odds = 0
    for i in range(a,b+1):
        if not is_even(i):
            sum_of_odds += i

    return sum_of_odds

print(sum_odd(2,7))


# <QUESTION 2: Palindrome function>
# write code that satisfies the following specs
# def is_palindrome(s):
# """ s is a string
# Returns True if s is a palindrome and False otherwise """
#   if s = "222" returns True
#   if s = "2222" returns True
#   if s = "abc" returns False

def is_palindrome(s):
    """

    :param s: string
    :return: True if s is a palindrome and False otherwise
    """
    if s[:] == s[::-1]:
        return True
    else:
        return False
print(is_palindrome("222"))
print(is_palindrome("2222"))
print(is_palindrome("abc"))


# <QUESTION 3: Evaluate Quadratic>
# def eval_quadratic(a, b, c, x):
# a, b, c: numerical values for the coefficients of a quadratic equation
# x: numerical value at which to evaluate the quadratic.
# Returns the value of the quadratic a×x² + b×x + c

def eval_quadratic(a,b,c,x):
    """

    :param a: b - c : numerical values for the coefficients of quadratic equation
    :param x: numerical value at which to evaluate the quadratic
    :return: value of the quadratic a×x² + b×x + c
    """
    return a*(x**2) + (b*x) + c

print(eval_quadratic(1,1,1,1))


# <QUESTION 4: Two Quadratics>
# def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
# a1, b1, c1: one set of coefficients of a quadratic equation
# a2, b2, c2: another set of coefficients of a quadratic equation
# x1, x2: values at which to evaluate the quadratics
# Evaluates one quadratic with coefficients a1, b1, c1, at x1.
# Evaluates another quadratic with coefficients a2, b2, c2, at x2.
# Prints the sum of the two evaluations. Does not return anything.

def two_quadratics(a1,b1,c1,x1,a2,b2,c2,x2):

    q1 = a1 * (x1 ** 2) + (b1 * x1) + c1
    q2 = a2 * (x2 ** 2) + (b2 * x2) + c2
    return q1+q2

print(two_quadratics(1,1,1,1,1,1,1,1))