# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"firstName": "John", "lastName": "Doe", "Age": "30"}'

# Parse to dict
user = json.loads(userJSON)
# print(user['firstName'])

# Convert dict to JSON
car = {'make': 'Ford', 'model': 'Mustand', 'year': 1969}
carJSON = json.dumps(car)
print(carJSON)