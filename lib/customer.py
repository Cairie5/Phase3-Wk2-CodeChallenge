#!/usr/bin/env python3

# Define a Customer class
class Customer:
    all_customers = []  # Class attribute to store all instances of Customer
    
    # Initialize a customer instance with given_name and family_name
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.full_name = None  # Initialize full_name to None
        self.set_full_name()   # Call the set_full_name method to set the full_name
        Customer.all_customers.append(self)  # Add the instance to the list of all customers
        
    # Set the given_name attribute
    def set_given_name(self, given_name):
        self.given_name = given_name
        
    # Set the family_name attribute
    def set_family_name(self, family_name):
        self.family_name = family_name
        
    # Set the full_name attribute by combining given_name and family_name
    def set_full_name(self):
        self.full_name = f"{self.given_name} {self.family_name}"
        
    # Class method to retrieve all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers

# Creating instances of the Customer class
mycustomer = Customer("George", "Washington")
newCustomer = Customer("Henry", "Kennedy")

# Accessing all customers and printing full names
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name)
