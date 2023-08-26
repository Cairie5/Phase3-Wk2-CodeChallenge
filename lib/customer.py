#!/usr/bin/env python3

class Customer:
    all_customers = []
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.full_name = None
        self.set_full_name()
        Customer.all_customers.append(self)
        
    def set_given_name(self, given_name):
        self.given_name = given_name

    def set_family_name(self, family_name):
        self.family_name = family_name

    def set_full_name(self):
        self.full_name = f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
    
mycustomer = Customer("George", "Washington")
newCustomer = Customer("Henry", "Kennedy")

# Accessing all customers and printing full names
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name)
