# >QUESTION 1a>
# simple example of a while loop using the zelda Lost Forest

where = input("You are in the Lost Forest: where would you like to go? right or left? ")
while where == "right":
    where = input("You are still lost in the forest: where would you like to go? right or left ")
print("You got out of the Lost Forest!")


# <QUESTION 1b>
# expand Lost forest example:
# add a :( face to the input question when the user answers "right" more than 2 times

where = input("You are in the Lost Forest: where would you like to go? right or left? ")
counter = 0
while where == "right":
    counter += 1
    if counter > 2:
        print(":(")
    where = input("You are still lost in the forest: where would you like to go? right or left ")
print("You got out of the Lost Forest!")


# <QUESTION 2>
# for loop example
# fix code from lecture:

# I added (mysum + end) in the print statement
mysum = 0
start = 3
end = 5
for i in range(start, end):
    mysum += i
print(mysum + end)

# OR adding +1 to end in for loop | solution from the lecture
mysum = 0
start = 3
end = 5
for i in range(start, end+1):
    mysum += i
print(mysum)


# <QUESTION 3>
# Assume you are given a positive integer variable named N
# write code that prints "hello world" on separate lines, N times
# you can use a while loop or a for loop

text = "hello world"
n = 4
for i in range(n):
    print(text)