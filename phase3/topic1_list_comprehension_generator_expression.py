# List Comprehensions and Generator Expressions
# List Comprehension - build a new list from an existing one in one line

#regular loop
prices = [999, 49, 199, 299, 149]
discounted = []
for p in prices:
    discounted.append(p * 0.9)

# same thing as a list comprehension
discounted = [p * 0.9 for p in prices]

# with a condition - only discount items above 100
discounted = [p * 0.9 for p in prices if p > 100]

#DICT comprehension is the same idea

# products = ['laptop', 'mouse', 'monitor']
prices = [999, 49, 199]

# catalog = {name: price for name, price in zip(products, prices)}
# --> {'laptop': 999, 'mouse': 49, 'monitor': 199}
# print(catalog)

# Generator expressions - like a list comprehension but doesn't build the whole list in memory, just computes on demand, use inside sum(), max(), min().

prices = [999, 49, 199, 299, 149]

total = sum(p * 0.9 for p in prices if p > 100)
highest = max(p * 0.9 for p in prices if p > 100)

# Exercise:
products = [
    {"name": "Laptop", "price": 999, "available": True},
    {"name": "Mouse", "price": 49, "available": False},
    {"name": "Keyboard", "price": 79, "available": True},
    {"name": "Monitor", "price": 349, "available": True},
    {"name": "Webcam", "price": 89, "available": False},
]

"""
Using comprehensions only (no regular for loops), produce:

A list of names of available products only
A list of prices with 10% discount applied — available products only
A dict of {name: price} for all products
The total value of available products using sum() and a generator
"""
available_products = [p["name"] for p in products if p["available"]]
discounted = [p["price"] * 0.9 for p in products if p["available"]]
catalog = {p["name"]: p["price"] for p in products}
total_value = sum(p["price"] for p in products if p["available"])

print(available_products)
print(discounted)
print(catalog)
print(total_value)