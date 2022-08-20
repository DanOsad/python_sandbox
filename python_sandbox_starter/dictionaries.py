# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Constructor
person2 = dict(first_name='Sara', last_name='Mighty', age=29)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key value pair
person['phone'] = '555-555-5555'

# Get keys
person.keys()

# Get items (values) # RETURNS TUPLES
person.items()

# Copy dict
person3 = person.copy()

# Remove item
del person['age']
person.pop('phone')

# Clear dict
person.clear()

# Get length
len(person3)

# List of dicts
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 55}
]

print(people[0]['name'])