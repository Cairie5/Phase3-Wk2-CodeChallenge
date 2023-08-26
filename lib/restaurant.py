#!/usr/bin/env python3

class Restaurant:
    def __init__(self, name=None):
        # Initialize the private attribute _name to None
        self._name = None
        # If a name is provided during initialization, call set_name method
        if name is not None:
            self.set_name(name)  
        
    def set_name(self, name):
        # Check if the input name is a string
        if isinstance(name, str):  
            # Update the private attribute _name with the provided name
            self._name = name  
    
    def get_name(self):
        # Return the value of the private attribute _name
        return self._name  

# Create an instance of the Restaurant class with the name "Dae Jang Geum"
restaurant = Restaurant("Dae Jang Geum")

# Use the get_name method to retrieve and print the restaurant name
print(restaurant.get_name())
