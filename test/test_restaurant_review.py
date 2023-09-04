import os
import sys
import pytest

# Add the project's root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.review import Review
from lib.restaurant import Restaurant
from lib.customer import Customer


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

# New test functions for additional test cases

def test_review_properties():
    # Test properties of the Review class
    # Creating an instance of the Review class
    myreview = Review("Patience", "Dae Jang Geum", 10)

    # Getting the rating of the review using the rating property
    assert myreview.rating == 10
    assert myreview.review_rating() == 10


def test_customer_properties():
    # Test properties of the Customer class
    # Creating instances of the Customer class
    mycustomer = Customer("George", "Washington")
    newCustomer = Customer("Sammy", "Junior")

    # Adding reviews and accessing reviewed restaurants for a customer
    restaurant1 = "Dae Jang Geum"
    restaurant2 = "Pizza Palace"

    mycustomer.add_review(restaurant1, 5)
    mycustomer.add_review(restaurant2, 4)

    # Using the new methods
    assert mycustomer.num_reviews() == 2

    found_customer = Customer.find_by_name("George Washington")
    assert found_customer.full_name == "George Washington"

    customers_with_given_name = Customer.find_all_by_given_name("Sammy")
    assert len(customers_with_given_name) == 2  # There are 2 customers with the given name "Sammy Junior"

def test_find_customer_by_name():
    # Test finding a customer by name
    # Creating instances of the Customer class
    customer1 = Customer("George", "Washington")
    customer2 = Customer("John", "Adams")

    # Find a customer by name
    found_customer = Customer.find_by_name("George Washington")
    assert found_customer.full_name == customer1.full_name  # Compare full names instead


if __name__ == "__main__":
    pytest.main()
    