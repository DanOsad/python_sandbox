# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Crate class
from validator import validate_email


class User:
    # Constructor
    def __init__(self, firstName, lastName, age, email):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
    def greeting(self):
        return f'My name is {self.firstName} {self.lastName} and I am {self.age} years old.'
    def checkEmail(self):
        return validate_email(self.email)

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, firstName, lastName, age, email):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.balance = 0
    
    def setBalance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.firstName} {self.lastName} and I am {self.age} years old. My balance is {self.balance}.'

# Init user object
brad = User("Brad", "Ardley", 31, "brdardly@gmail.com")
janet = Customer('Janet', "Johnson", 24, 'janet@yahoo.com')

janet.setBalance(500)
print(janet.greeting())