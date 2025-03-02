# <QUESTION 1>
# Assume you are given a positive integer variable named N.
# Write a piece of Python code that finds the cube root of N.
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube.
# Hint: use a loop that increments a counter—you decide when the counter should stop.

n = 8
i = 1

while i ** 3 < n:
    i += 1
if i ** 3 == n:
    print(i)
else:
    print("error")


# <QUESTION 2>
# Write a for loop over these ranges and prints how many even numbers are in that range
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)

count = 0

for i in range(10):
    if i % 2 == 0:
        count += 1
print("even numbers:",count)


# <QUESTION 3>
# Assume you are given a string of lowercase letters in variable s
# count how many unique letters there are in the string
# "abca" = 3

seen = ""
count = 0
s = "abcaddddefefef"
for char in s:
    if char not in seen:
        seen += char
        count += 1 #not needed if using print len()
print("unique letters:",count)
# or
# this eliminates the need for a count variable, we can just count how many chars in seen string using len()
print("unique letters:",len(seen))


# <QUESTION 4a>
# GUESS AND CHECK - SQUARE ROOT / WHILE LOOP EXAMPLE / DOESN'T WORK FOR NEGATIVES

guess = 0
x = int(input("Enter an integer: "))

while guess ** 2 < x:
    guess += 1
if guess ** 2 == x:
    print("Square root of",x,"is",guess)
else:
    print(x,"is not a perfect square")


# <QUESTION 4b>
# GUESS AND CHECK - ADJUSTING FOR A NEGATIVE VALUE
# ADDED neg_flag to check for negative input to redirect user
guess = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while guess ** 2 < x:
    guess += 1
if guess ** 2 == x:
    print("Square root of",x,"is",guess)
else:
    print(x,"is not a perfect square")
    if neg_flag:
        print("Just checking.... did you mean",-x,"?")


# <QUESTION 4c>
# GUESS AND CHECK CUBE ROOT / USING FOR LOOP / CHECKING FOR NEGATIVES

cube = int(input("Enter an integer: "))
# using abs() to cast number as absolute
# cube + 1 because we want to include the number 1 if the input is 1...
#... otherwise it would just loop through 0 and stop before getting to 1
for guess in range(abs(cube)+1):
    if guess ** 3 >= abs(cube):
        break # Terminating check once we know we have passed possible answer
if guess ** 3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("cube root of",cube,"is",guess)


# <QUESTION 5>
# hardcode a secret number
# write a program that checks through all the numbers from 1 to 10
# and prints the secret value if it's in that range
# if it's not found, it prints that it couldn't find it

secret = 9
found = False
# range is (1,2,3,4,5,6,7,8,9,10)
for i in range (1,11):
    if i == secret:
        found = True
if found:
    print("found it:", secret)
else:
    print("i couldn't find it...")


# <QUESTION 6a>
# GUESS AND CHECK / WORD PROBLEMS
# Alyssa, Ben and Cindy are selling tickets to a fundraiser
# Ben sells 2 fewer than Alyssa
# Cindy sells twice as many as Alyssa
# 10 total tickets were sold
# How many did Alyssa sell?

for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total = (alyssa + ben + cindy == 10)
            two_less = (ben == alyssa - 2)
            twice = (cindy == 2 * alyssa)
            if total and two_less and twice:
                print(f"Alyssa sold {alyssa} tickets")
                print(f"Ben sold {ben} tickets")
                print(f"Cindy sold {cindy} tickets")


# <QUESTION 6b>
# GUESS AND CHECK / WORD PROBLEMS / BIGGER NUMBERS / MORE EFFICIENT
# Alyssa, Ben and Cindy are selling tickets to a fundraiser
# Ben sells 20 fewer than Alyssa
# Cindy sells twice as many as Alyssa
# 1000 total tickets were sold
# How many did Alyssa sell?
# /the previous code wont end in a reasonable time/

for alyssa in range(1001):
    ben = max(alyssa - 20,0)
    cindy = alyssa * 2
    if ben + cindy + alyssa == 1000:
        print(f"Alyssa sold {alyssa} tickets")
        print(f"Ben sold {ben} tickets")
        print(f"Cindy sold {cindy} tickets")