# Example of how incrementing decimals does not equate to whole number
x = 0
for i in range(10):
    x += 0.1
print(x == 1)
print(x, "==", 10*0.1)


# <CONVERTING INTEGER TO BINARY (base 2)>
num = -345

if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False
result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num%2) + result # prepending remainder of num/2 to the result string
    num = num//2 # floor division rounds result to nearest integer <= result e.g. 9//2 = 4.5 -> 4
if is_neg:
    result = "-" + result
print(result)


# <CONVERTING FRACTION TO BINARY (base 2)> (works for fractions that can convert to whole numbers by multiplying with a power of 2)

x = 0.625

p = 0
while ((2**p)*x)% 1 != 0: # % grabs the decimal only so 1.1 gives 0.1
    print("Remainder =", str((2**p)*x - int((2**p)*x))) # subtracts the integer part of the float number, leaving only the remaining decimals
    p += 1

num = int((2**p)*x)

# converting integer to binary (base 2)
result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num%2) + result
    num = num//2

## adds a decimal point -p times to left of result ##
for i in range(p - len(result)):
    result = "0" + result

result = result[0:-p] + "." + result[-p:]
#####################################################
print("The binary representation of the decimal", str(x), "is", str(result))


# <APPROXIMATION ALGORITHM>
# similar to guess-and-check but:
#   1. we increment by a small amount
#   2. we stop when close enough (exact is not possible)

x = 534 # value we want to find approximate square root of
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001 # if fail to find square root(overshooting) - can decrease increment...
#...smaller increment means more values are checked

# abs is there for negative inputs**
# loop stops when (guess ** 2 - x) reaches the epsilon range (smallest possible amount)...
#...AND when guess ** 2 goes past the last reasonable guess (this prevents over-shooting epsilon)
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1 # tracks number of guesses

print(f"num_guesses = {num_guesses}")
if abs(guess**2 - x) >= epsilon:
    print(f"Failed on square root of {x}") # condition runs if passed reasonable guess
    print(f"Last guess was {guess}")
    print(f"Last guess squared is {guess**2}")
else:
    print(f"{guess} is close to square root of {x}")

# LESSONS LEARNED IN APPROXIMATION #
# Never use == to compare floats in the stopping condition
# Need to be careful of infinite loop due to overshooting the 'close-enough' stopping condition
# Tradeoff exists between efficiency of algorithm and accuracy of result
# Need to think about how close an answer we want when setting parameters of algorithm
