#!/usr/bin/env python3

class Review:
    # Class attribute to store all instances of Review
    all_reviews = []

    def __init__(self, customer, restaurant, rating=None):
        # Initialize instance attributes
        self.customer = customer
        self.restaurant = restaurant
        self._rating = None  # Initialize the private attribute _rating
        
        # Add the review instance to the all_reviews list
        Review.all_reviews.append(self)

        # If a rating is provided during initialization, call set_rating method
        if rating is not None:
            self.set_rating(rating)

    def get_rating(self):
        return self._rating  # Getter method to retrieve the private rating attribute

    def set_rating(self, rating):
        if isinstance(rating, int):
            self._rating = rating  # Setter method to update the private rating attribute
        else:
            print("Rating must be an integer")

    # Create a property named 'rating'
    rating = property(get_rating, set_rating)

    def get_customer(self):
        return self.customer  # Getter method to retrieve the customer attribute

    def get_restaurant(self):
        return self.restaurant  # Getter method to retrieve the restaurant attribute

    @property
    def restaurant_name(self):  # Property to retrieve the restaurant name
        return self.restaurant

    @classmethod
    def all(cls):
        # Return a list of formatted strings containing customer, restaurant, and rating information
        return [
            f"Customer: {review.get_customer()}, Restaurant: {review.restaurant_name}, Rating: {review.rating}"
            for review in cls.all_reviews
        ]

# Creating an instance of the review class
myreview = Review("Patience", "Dae Jang Geum", 10)

# Getting the rating of the review using the rating property
print(myreview.rating)

# Getting all the reviews
all_reviews = Review.all()
print(all_reviews)

