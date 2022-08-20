# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
fruits3 = ('Apples',) # NEED TRAILING COMMA FOR SINGLE VALUE TUPLE

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits3

# Length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apples', 'Oranges', 'Mangoes'}

# Check if in set
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grapes')
print(fruit_set)

# Remove from set
fruit_set.remove('Grapes')

# Clear set (different from deleting)
fruit_set.clear()

# Delete set
del fruit_set