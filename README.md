# Phase3-Wk2-CodeChallenge

Welcome to the Object Relations Code Challenge! In this assignment, you will work with three classes: `Restaurant`, `Customer`, and `Review`. The goal is to implement methods that establish relationships between these classes and provide functionality to interact with them.

## Challenge 1: Customer Class

### Problem Explanation

In this challenge, you'll implement methods for the `Customer` class that represents customers who can write reviews for restaurants.

### Solution Explanation

The `Customer` class has attributes for the given name and family name of the customer. The `set_given_name` and `set_family_name` methods allow you to update these attributes. The `set_full_name` method combines the given name and family name to create the full name. The `all` class method returns a list of all customer instances.

## Challenge 2: Restaurant Class

### Problem Explanation

In this challenge, you'll implement methods for the `Restaurant` class that represents restaurants and their relationships with customers.

### Solution Explanation

The `Restaurant` class has attributes for the restaurant's name. The `name` method returns the name of the restaurant. The `reviews` method returns a list of reviews for the restaurant, and the `customers` method returns a list of unique customers who reviewed the restaurant.

## Challenge 3: Review Class

### Problem Explanation

In this challenge, you'll implement methods for the `Review` class that represents reviews written by customers for restaurants.

### Solution Explanation

The `Review` class has attributes for the customer, restaurant, and rating of the review. The `customer` and `restaurant` methods return the corresponding objects. The `rating` method returns the rating. The `all` class method returns a list of all reviews.

## Instructions

1. Implement the methods described for each class.
2. Create instances of the classes and test your methods in the console.
3. Focus on writing methods that work before aiming for completeness.
4. Save and run your code to verify it works as expected.

## Setup & Pre-requisite Data
git clone the repository to your local machine using the command.
```bash
$ git clone git@github.com:Cairie5/Phase3-Wk2-CodeChallenge.git
```

Navigate to the project using the command cd
```bash
$ cd phase3-Wk2-CodeChallenge
```

Run the code using the command code . on your terminal
```bash
$ code .
```

Install the necessary dependencies required
```bash
$ pipenv install
```
```bash
 $ pipenv shell
```

## Technologies Used
. Python

## Author
The author of this script is Patience Wangari Muraguri.

## License
MIT License Copyright (c) [2023] [Patience Muraguri]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
