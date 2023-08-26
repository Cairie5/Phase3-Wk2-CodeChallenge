class  Customer:
    all_customers = []
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.full_name = None
        self.set_full_name()
        Customer.all_customers.append(self)
        
    def set_given_name(self):
        return self.given_name
    
    def set_family_name(self):
        return self.family_name
    
    def set_full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers
    
# Creating instances of the Customer class
mycustomer = Customer("George", "Washington")
newCustomer = Customer("Henry", "Kennedy")

# Calling the set_full_name method for each instance (usually done within __init__)
mycustomer.set_full_name()
newCustomer.set_full_name()

# Accessing all customers and printing full names
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name)
    