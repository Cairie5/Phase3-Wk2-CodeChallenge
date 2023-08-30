#!/usr/bin/env python3

from lib.review import Review

# Define a Customer class
class Customer:
    all_customers = []  # Class attribute to store all instances of Customer
    
    # Initialize a customer instance with given_name and family_name
    def __init__(self, given_name, family_name):
        self.given_name = given_name  # Convert given_name to string
        self.family_name = family_name  # Convert family_name to string
        self.full_name = None  # Initialize full_name to None
        self.set_full_name()   # Call the set_full_name method to set the full_name
        self.reviews = []      # List to store associated reviews
        Customer.all_customers.append(self)  # Add the instance to the list of all customers
        
    # Set the given_name attribute
    def set_given_name(self, given_name):
        if isinstance(given_name, str):
            self.given_name = given_name
        else:
            print("Given name must be a string")
        
    # Set the family_name attribute
    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            self.family_name = family_name
        else:
            print("Family name must be a string")
        
    # Set the full_name attribute by combining given_name and family_name
    def set_full_name(self):
        self.full_name = f"{self.given_name} {self.family_name}"
        
    # Class method to retrieve all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        # Returns a unique list of all restaurants this customer has reviewed
        reviewed_restaurants = set()
        for review in self.reviews:
            reviewed_restaurants.add(review.restaurant)
        return list(reviewed_restaurants)

    def add_review(self, restaurant, rating):
        # Creates a new review and associates it with this customer and restaurant
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    def num_reviews(self):
        # Returns the total number of reviews that this customer has authored
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        # Given a string of a full name, returns the first customer whose full name matches
        for customer in cls.all_customers:
            if customer.full_name == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        # Given a string of a given name, returns a list containing all customers with that given name
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers

# Creating instances of the Customer class
mycustomer = Customer("George", "Washington")
newCustomer = Customer("Sammy", "Junior")

# Adding reviews and accessing reviewed restaurants for a customer
restaurant1 = "Dae Jang Geum"
restaurant2 = "Pizza Palace"

mycustomer.add_review(restaurant1, 5)
mycustomer.add_review(restaurant2, 4)

# Using the new methods
print("Number of reviews by George Washington:", mycustomer.num_reviews())

found_customer = Customer.find_by_name("George Washington")
if found_customer:
    print("Found customer:", found_customer.full_name)
else:
    print("Customer not found.")

customers_with_given_name = Customer.find_all_by_given_name("Sammy")
print("Customers with given name 'Sammy':")
for customer in customers_with_given_name:
    print(customer.full_name)
