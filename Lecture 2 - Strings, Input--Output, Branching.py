# <QUESTION 1>
# Assume you are given a variable named 'number' (has a numerical vaue).
# Write a piece of Python code that prints out one of the following strings:
# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero


# <QUESTION 2>
# Write a program that:
#   asks the user for a verb
#   prints "I can _ better than you" where you replace _ with the verb
#   then prints the verb 5 times in a row separated by spaces.

s1 = input("input verb: ")
# This variable was not needed as I can use print expression with commas as below.
s2 = "I can " + s1 + " better than you!"
print(s2)
# Alternate way to use print, more efficient -- use commas to insert spaces automatically
print("I can",s1,"better than you!")
print((s1 + " ") * 5)
# Printing "verb" 5 times but deleting the extra space at the end.
# Basically slicing the original expression to a new subset including every index(character) but the last one.
print(((s1 + " ") * 5)[:-1])


# <QUESTION 3>
# write a program that:
#   saves a secret number in a variable
#   Asks the user for a number to guess
#   Prints a bool "False" or "True" if the number was guessed correctly

secret = 13
guess = int(input("input guess: "))
print(guess == secret)


# <QUESTION 4>
#   write a program that:
#   saves a secret number
#   Asks the user for a number to guess
#   prints whether the guess is too low, too high, or the same as secret

secret = 13
guess = int(input("input guess: "))
if guess == secret:
    print("guess was correct!")
elif guess < secret:
    print("guess was too low...")
elif guess > secret:
    print("guess was too high...")
