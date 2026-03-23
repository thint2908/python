# these are functional programming tools - useful to recognize and read, even if you don't write them constantly
# LAMBDA - a tiny anonymous function, one expression only

# regular function
def double(x):
    return x * 2

# same thing as a lambda
double = lambda x: x * 2

# with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

# map() - apply a function to every item in a list:

prices = [999, 49, 199, 299, 149]
discounted = list(map(lambda p : p * 0.9, prices))
# -> [899.1, 44.1, 179.1, 269.1, 134.1]
print(discounted)

#filter() - keep only items where the function returns True:

expensive = list(filter(lambda p: p > 100, prices))
print(expensive)  # [999, 199, 299, 149]

# sort products by price
# products.sort(key=lambda p: p["price"])

# sort by name alphabetically
# products.sort(key=lambda p: p["name"])

# that key=lambda pattern is the most common real-world use of lambda.

"""
🏋️ Exercise
Using the same products list from before:

Use sorted() with a lambda to sort products by price low to high
Use sorted() with a lambda to sort by name alphabetically
Use filter() + lambda to get only unavailable products
Use map() + lambda to create a list of strings like "Laptop: $999"
"""

products = [
    {"name": "Laptop", "price": 999, "available": True},
    {"name": "Mouse", "price": 49, "available": False},
    {"name": "Keyboard", "price": 79, "available": True},
    {"name": "Monitor", "price": 349, "available": True},
    {"name": "Webcam", "price": 89, "available": False},
]

sorted_by_price = sorted(products, key=lambda p: p["price"])
sorted_by_name = sorted(products, key=lambda p: p["name"])
unavailable = list(filter(lambda p: not p["available"], products))
formatted = list(map(lambda p: f"{p['name']}: ${p['price']}", products))

print(sorted_by_price)
print(sorted_by_name)
print(unavailable)
print(formatted)