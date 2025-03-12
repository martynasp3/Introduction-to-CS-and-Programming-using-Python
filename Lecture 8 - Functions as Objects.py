def is_even(x):
    return x % 2 ==0

# <QUESTION 1>
# fix the code that tries to write this function
def is_triangular(n):
    """
    :param n: int > 0
    :return: True if n is triangular, False otherwise
    """
    total = 0
    for i in range(n+1):
        total += i
        if total > 0 and total ==  n:
            return True
    return False

print(is_triangular(1))
print(is_triangular(4))
print(is_triangular(6))


# <BISECTION SEARCH AS A FUNCTION>
def bisection_root(x):
    """

    :param x: positive int > 1
    :return: approximation to the square root of x
    """
    epsilon = 0.01
    low = 0
    high = x
    guess = (high + low)/2.0
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

print(bisection_root(16))
print(bisection_root(1345))
print(bisection_root(124))

# <QUESTION 2>
# write a function that satisfies the following specs:
# def count_nums_with_sqrt_close_to (n, epsilon):
# """
# params n: n is an int > 2
# params epsilon: epsilon is a positive number < 1
# return: how many integers have a square root within epsilon of n
# """
# use bisection_root to get an approx. for the sqrt of an integer
# e.g. print(count_nums_with_sqrt_close_to(10, 0.1)

def count_nums_with_sqrt_close_to (n, epsilon):
    count = 0
    for i in range (n**3):
        sqrt = bisection_root(i)
        if abs(sqrt - n) < epsilon:
            count+=1
    return count

print(count_nums_with_sqrt_close_to(10, 0.1))


# <FUNCTIONS AS PARAMETERS>

def calc(op,x,y):
    return op(x,y) # returns a function call where 'op' is the function

def add(a,b):
    return a+b

def div(a,b):
    if b!= 0:
        return a/b
    print("Denom was 0.")

res = calc(add,2,3) # returns add(2,3) -> None


# <QUESTION 2>
# write a function that meets these specs.
# def apply(criteria, n):
# """
# criteria is a func that takes in a number and returns a bool
# n is an int
# returns how many ints from 0 to n (inclusive) match the criteria
# (i.e. return True when run with criteria)
# """
# using is_even() function as an example for criteria

def apply (criteria, n):
    count = 0
    for i in range(0,n+1):
        if criteria(i):
            count += 1
    return count

how_many = apply(is_even,10)
print(how_many)