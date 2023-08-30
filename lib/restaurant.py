#!/usr/bin/env python3

from lib.review import Review

class Restaurant:
    def __init__(self, name=None):
        self._name = None
        if name is not None:
            self.set_name(name)
        self.reviews = []

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name

    def get_name(self):
        return self._name

    def reviews(self):
        return [review for review in self.reviews]

    def customers(self):
        reviewed_customers = set()
        for review in self.reviews:
            reviewed_customers.add(review.customer())
        return list(reviewed_customers)

    def add_review(self, customer, rating):
        new_review = Review(customer, self, rating)
        self.reviews.append(new_review)

    def all_reviews(self):
        return self.reviews

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
