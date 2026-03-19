def greet(name):
    return f"Hello, {name}!"

#print(greet("Thint"))

# Parameters wit default values
def create_product(name, price, available=True):
    return f"{name} costs {price}, available: {available}"

# print(create_product("Laptop", 999.69))
# print(create_product("Old item", 49.99, False))

"""
### 🏋️ Exercise

Write a function called `product_summary` that:
- Takes `name`, `price`, and `quantity` as parameters
- Calculates `total_value = price * quantity`
- Returns a formatted string like:
```
Laptop | Price: 999 | Qty: 5 | Total Value: 4995
"""

def product_summary(name, price, quantity):
    total_value = price * quantity
    return f"{name} | Price: {price} | Qty: {quantity} | Total Value: {total_value}"

print(product_summary("Laptop", 999, 5))