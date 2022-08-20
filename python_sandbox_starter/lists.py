# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numers2 = list((1,2,3,4,5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append
fruits.append('Mangoes')

# Remove
fruits.remove('Grapes')

# Insert
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse
fruits.reverse()

# Sort
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)