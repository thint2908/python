#TOPIC 1: Variables and Data Types

product_name = "Laptop"
price = 999.69
quantity = 5
available = True

print("Product Name:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Available:", available)


#TOPIC 2: Comparison Operators

price > 100 # True
quantity == 0 # False
available != False # True

# Arithmetic 
total = price * quantity # 4998.45
discount = 0.1 * price # 99.969

# if / else / elif 
if quantity == 0:
    print("Out of stock")
elif quantity < 5:
    print("Low stock warning")
else:
    print("In stock")
    
    
if not available:
    print("Product is not listed for sale")
elif price > 500:
    print("Product is expensive")
elif price >= 100 and price <= 500:
    print("Affordable product")
elif price < 100:
    print("Cheap product")
    