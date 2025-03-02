# <PROBLEM SET 1; PART A: Saving for a House>
# find the number of months it takes to save up for a down payment
# cost of down payment is calculated by multiplying total cost of house by down payment %
# user inputs (cast as floats):
#   1. the starting yearly salary (yearly_salary)
#   2. the portion of salary to be saved (portion_saved) *in decimal form*
#   3. the cost of your dream home (cost_of_dream_home)
# Assume portion_down_payment = 0.25
# Annual rate of return at the end of each month - amount_saved * r/12 (r=0.05)

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Enter the starting yearly salary: "))
portion_saved_percent = float(input("Enter the percent of the salary to be saved: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
amount_saved = float(0)
r = 0.05
months = 0
yearly_savings = yearly_salary * portion_saved_percent
monthly_savings = yearly_savings / 12
down_payment = cost_of_dream_home * portion_down_payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################

while amount_saved < down_payment:
    amount_saved += amount_saved * r/12 # calculates annual rate of return using start of month amount
    amount_saved += monthly_savings # monthly salary incremented
    months += 1
print(f"number of months: {months}")


# <PROBLEM SET 1; PART B: Saving with a raise>
# adding a salary raise every 6 months
# extra input 4. (semi_annual_raise), decimal percentage
# yearly_salary increases by semi_annual_raise at the end of every 6 months.

yearly_salary = float(input("Enter the starting yearly salary: "))
portion_saved_percent = float(input("Enter the percent of the salary to be saved: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise  = float(input("Enter the semi annual raise percentage: "))

portion_down_payment = 0.25
amount_saved = float(0)
r = 0.05
months = 0
yearly_savings = yearly_salary * portion_saved_percent
monthly_savings = yearly_savings / 12
down_payment = cost_of_dream_home * portion_down_payment

while amount_saved < down_payment:
    amount_saved += amount_saved * r/12 # calculates annual rate of return using start of month amount
    amount_saved += monthly_savings # monthly salary incremented
    months += 1
    if months % 6 == 0 and months != 0: # if 6 months have passed, increase yearly salary and adjust savings variables
        yearly_salary = yearly_salary * (1+semi_annual_raise)
        yearly_savings = yearly_salary * portion_saved_percent
        monthly_savings = yearly_savings / 12

print(f"number of months: {months}")


# <PROBLEM SET 1; PART C: Choosing an Interest Rate>
# Bisection search - Lecture 6

initial_deposit = float(input("Enter the amount in your savings account: "))
cost_of_dream_home = float(800000)
down_payment = cost_of_dream_home * 0.25
