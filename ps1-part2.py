# Write a function that takes two variables and does all the computations asked
def number_fun(a,b):
# Repeat back the numbers
    print(f'You entered {a} and {b}')
# Perform calculations. Be careful about string formatting for autograders.
    s = a + b
    print(f'{a} + {b} = {s}')
    p = a * b
    print(f'{a} * {b} = {p}')
    r = a ** b
    print(f'{a} ** {b} = {r}')
    d = a % b
    print(f'{a} % {b} = {d}')

# Ask the user for the first number, store the value in a variable


# Ask the user for the second number, store the value in a variable

firstnum = float(input('Enter a integer between 10 and 100'))
secondnum = float(input('Enter a integer less than 4'))

number_fun(firstnum,secondnum)
