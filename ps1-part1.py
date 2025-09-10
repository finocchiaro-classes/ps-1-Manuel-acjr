# These lines are asking the user to input two number. I put float just in case they add a decimal.
firstnum = float(input('Enter a interger bewteen 10-100'))
secondnum = float(input('Enter a integer less than 4'))
# This is telling you the numbers the user has entered
print(f'You entered {firstnum} and {secondnum}')
# Sum of the two numbers
s = firstnum + secondnum
# Prints the sum
print(f'{firstnum} + {secondnum} = {s}')
# Product of the two numbers
p = firstnum * secondnum
# Print product
print(f'{firstnum} * {secondnum} = {p}')
# First num raised to second num
r = firstnum ** secondnum
# Print answer
print(f'{firstnum} ** {secondnum} = {r}')
# Use % to get remainder of the two numbers when divided
d = firstnum % secondnum
# Print answer
print(f'{firstnum} % {secondnum} = {d}')
