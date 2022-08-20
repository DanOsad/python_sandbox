# If/ Else conditions are used to decide to do something based on something being true or false
x = 10
y = 5


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > y:
    print(f'{x} is greater than {y}')
else: 
    print(f'{y} is greater than {x}')

# Elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else: 
    print(f'{y} is greater than {x}')

# Nested if
if x > 2:
    if x < 10:
        print(x)

# Logical operators (and, or, not) - Used to combine conditional statements

# And
if x > 2 and x < 10:
    print(x)

# Or
if x > 2 or x < 10:
    print(x)

# Not
if not(x==y):
    print(x,y)


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6,7,8,9, 10]

# In
if x in numbers:
    print(x in numbers)

# Not in
if y not in numbers:
    print(y not in numbers)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Is
if x is y:
    print(x is y)

# Is not
if x is not y:
    print(x is not y)