import os
import sys
import pytest

# Add the project's root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.restaurant import Restaurant
from lib.customer import Customer
from lib.review import Review

def test_restaurant_name():
    restaurant = Restaurant("Dae Jang Geum")
    assert restaurant.get_name() == "Dae Jang Geum"

def test_customer_given_name():
    customer = Customer("George", "Washington")
    assert customer.given_name == "George"

def test_customer_family_name():
    customer = Customer("George", "Washington")
    assert customer.family_name == "Washington"

def test_customer_full_name():
    customer = Customer("George", "Washington")
    assert customer.full_name == "George Washington"

def test_review_rating():
    restaurant = Restaurant("Dae Jang Geum")
    customer = Customer("George", "Washington")
    review = Review(customer, restaurant, 5)
    assert review.rating == 5

def test_customer_restaurants():
    customer = Customer("George", "Washington")
    restaurant1 = Restaurant("Restaurant A")
    restaurant2 = Restaurant("Restaurant B")

    customer.add_review(restaurant1, 4)
    customer.add_review(restaurant2, 5)

    reviewed_restaurants = customer.customer_reviews()
    assert len(reviewed_restaurants) == 2
    assert restaurant1 == reviewed_restaurants[0]
    assert restaurant2 == reviewed_restaurants[1]

# Add more test functions for other methods

if __name__ == "__main__":
    pytest.main()
