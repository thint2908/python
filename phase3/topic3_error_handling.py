# Basic structure
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")

# Catch multiple specific errors
try:
    value = int("abc")
except ValueError:
    print("That's not a number")
except TypeError:
    print("Wrong type entirely")

# Catch any error (use sparingly)
try:
    something_risky()
except Exception as e:
    print(f"Something went wrong: {e}")

# finally — always runs, even if there's an error
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Done attempting to read file")

# raising your own errors - you'll do this in Odoo to block invalid actions:

def set_price(self, price):
    if price < 0:
        raise ValueError("Price can't be negative: {price}")
    self.price = price

# in Odoo specifically you'll use raise UserError("msg") instead of ValueError - but the concept is identical

"""
🏋️ Exercise
Write a function safe_divide(a, b) that:

Returns a / b normally
Catches ZeroDivisionError and returns "Error: division by zero"
Catches TypeError and returns "Error: invalid input type"
Always prints "Operation complete" in a finally block

Then write a class Product with a set_price() method that:

Accepts a new price
Raises ValueError with a clear message if price is negative or zero
Sets self.price if valid


"""

def safe_divide(a, b):
    try:
        return a /b
    except ZeroDivisionError:
        return "Error: division by zero"
    except TypeError:
        return "Error: invalid input type"
    finally:        
        print("Operation complete") 
    
class Product:
    def set_price(self, price):
        if price <= 0:
            raise ValueError(f"Price must be positive: {price}")
        self.price = price
        return f"Price set to {self.price}"
        
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))

p = Product()
for test_price in [20, -5, 0]:
    try:
        print(p.set_price(test_price))
    except ValueError as e:
        print(f"Caught: {e}")