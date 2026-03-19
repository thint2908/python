class Product:
    currency = "VND"
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    # Regular instance method - works with self (the object)
    def discount_price(self, percent):
        return self.price * (1 - percent)
    
    # Class method - works with the class it self, not an object
    @classmethod
    def get_currency(cls):
        return cls.currency
    
    # Static method - no access to objects or class, just a utility function
    @staticmethod
    def is_valid_price(price):
        return price > 0
    
laptop = Product("Laptop", 999.0)
print(laptop.discount_price(0.1)) # -> 899.1
print(Product.get_currency()) # -> VND
print(Product.is_valid_price(-5)) # -> False


"""
Extend your Customer class with:

A class attribute total_customers = 0 — increment it every time a new customer is created
A class method get_total() that returns "Total customers: X"
A static method is_valid_email(email) that returns True if "@" is in the email, False otherwise

Then:

Create 3 customer objects
Print Customer.get_total()
Test Customer.is_valid_email() with a valid and an invalid email
"""

class Customer:
    total_customers = 0
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Customer.total_customers += 1
        
    @classmethod
    def get_total(cls):
        return f"Total customers: {cls.total_customers}"
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email

# Create 3 customer objects
customer1 = Customer("Alice", "alice@example.com")
customer2 = Customer("Bob", "bob@example.com")
customer3 = Customer("Charlie", "charlie@example.com")

# Print Customer.get_total()
print(Customer.get_total())  # -> Total customers: 3

# Test Customer.is_valid_email() with a valid and an invalid email
print(Customer.is_valid_email("alice@example.com"))  # -> True
print(Customer.is_valid_email("invalid-email"))     # -> False