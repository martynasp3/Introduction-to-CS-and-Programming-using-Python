# <BISECTION SEARCH>
# WAY FASTER THAN APPROXIMATION ALGORITHM, (LOGARITHMIC)
# Conditions;
#   - The search space has an order (e.g. numerical)
#   - We can tell whether guess was too low or too high (feedback)


# This code doesnt work for x values 0 < x < 1
x = 60
epsilon = 0.01
num_guesses= 0.0
low = 0
high = x
guess = (high+low)/2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x: # if guess**2 is less than x, guess becomes the new low endpoint
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f"number of guesses: {num_guesses}")
print(f"{guess} is close to square root of: {x}")


# Bisection Search - Square root with 0 < x < 1

x = 0.5
epsilon = 0.01
num_guesses= 0.0
low = x #square root of a number 0 < x < 1 cant be lower than number
high = 1 #cant be higher than 1
guess = (high+low)/2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f"number of guesses: {num_guesses}")
print(f"{guess} is close to square root of: {x}")


# BISECTION SEARCH FOR ANY VALUE #

x = 323
epsilon = 0.01
num_guesses= 0.0

# Checks if value is below 1. This will affect the low and high variables
if x >= 1:
    low = 1.0
    high = x
elif x > 0:
    low = x
    high = 1.0

guess = (high + low)/2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f"number of guesses: {num_guesses}")
print(f"{guess} is close to square root of: {x}")


# <QUESTION 1>
# find cube root of 27

cube = 27
epsilon = 0.01
low = 0
high = cube
num_guesses = 0
guess = (high + low) / 2.0

while abs (guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    elif guess**3 > cube:
        high = guess
    guess = (high + low) / 2.0
    num_guesses  += 1
print(f"cube root of {cube} is {guess}")
print(f"number of guesses: {num_guesses}")


# <NEWTON-RAPHSON ALGORITHM>
# Find roots of a polynomial in one variable
# Simple case for a polynomial: f(x) = x² - k (k is value you want to find square of)
# Formula:  g - (g² - k) / 2g
# ***Can only use it to find roots of values

epsilon = 0.01
k = 24.0
guess =  k/2.0
num_guesses = 0

while abs (guess**2 - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k) / (2*guess))
print(f"num_guesses: {num_guesses}")
print(f"square root of {k} is about {guess}")