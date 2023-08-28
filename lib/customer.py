#!/usr/bin/env python3

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

# Adding the Review class from the previous code
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating=None):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = None
        Review.all_reviews.append(self)
        if rating is not None:
            self.set_rating(rating)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if isinstance(rating, int):
            self._rating = rating
        else:
            print("Rating must be an integer")

    rating = property(get_rating, set_rating)

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @property
    def restaurant_name(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return [
            f"Customer: {review.customer()}, Restaurant: {review.restaurant_name}, Rating: {review.rating}"
            for review in cls.all_reviews
        ]

# Creating instances of the Customer class
mycustomer = Customer("George", "Washington")
newCustomer = Customer("Henry", "Kennedy")

# Accessing all customers and printing full names
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name)

# Adding reviews and accessing reviewed restaurants for a customer
restaurant1 = "Dae Jang Geum"
restaurant2 = "Pizza Palace"

mycustomer.add_review(restaurant1, 5)
mycustomer.add_review(restaurant2, 4)

print("Reviewed Restaurants:", mycustomer.restaurants())

# Getting all the reviews
all_reviews = Review.all()
print(all_reviews)
