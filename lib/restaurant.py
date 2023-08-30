#!/usr/bin/env python3

from lib.review import Review  # Import the Review class from the 'lib' module

class Restaurant:
    def __init__(self, name=None):
        self._name = None  # Initialize the name attribute
        if name is not None:
            self.set_name(name)  # If name is provided, set it using the set_name method
        self.reviews = []  # Initialize an empty list to store reviews

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name  # Set the name attribute only if it's a string

    def get_name(self):
        return self._name  # Return the name attribute

    def reviews(self):
        return [review for review in self.reviews]  # Return a list of reviews

    def customers(self):
        reviewed_customers = set()
        for review in self.reviews:
            reviewed_customers.add(review.customer())  # Collect customers who reviewed the restaurant
        return list(reviewed_customers)  # Return the list of reviewed customers

    def add_review(self, customer, rating):
        new_review = Review(customer, self, rating)  # Create a new Review instance
        self.reviews.append(new_review)  # Add the review to the list of reviews

    def all_reviews(self):
        return self.reviews  # Return the list of all reviews

# Create an instance of the Restaurant class with the name "Dae Jang Geum"
restaurant = Restaurant("Dae Jang Geum")

# Use the get_name method to retrieve and print the restaurant name
print(restaurant.get_name())

# Add a review for the restaurant
customer = "John Doe"
rating = 4
restaurant.add_review(customer, rating)

# Retrieve all reviews for the restaurant
print("All Reviews:")
for review in restaurant.all_reviews():
    print(f"Customer: {review.customer()}, Rating: {review.rating}")

# Retrieve all customers who reviewed the restaurant
print("Reviewed Customers:", restaurant.customers())
