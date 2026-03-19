# LIST - ordered, changeable, allows duplicates

products = ['laptop', 'mouse', 'laptop']
products.append('keyboard')
products.remove('mouse')
products[0]  # access by index --> 'laptop


# TUPLE - ordered, NOT changeable, (immutable)

dimensions = (30, 20, 5) #with, height, depth
dimensions[0] # -> 30
#dimensions[0] = 99 -> X will throw an error

#DICTIONARY - key-value pairs, like a record/row in Odoo

product = {
    "name": "laptop",
    "price": 999,
    "available" : True
}

product['name'] # -> 'laptop'
product['price'] = 899 # change the price   
product['brand'] = 'Dell' # add a new key-value pair

# SET - unordered, No duplicates

tags = {"sale", "new", "sale"} # -> {"sale", "new"} -> duplicates are removed
tags.add("featured") # add a new tag


"""
list use [], have method like: append, remove, pop, sort,.... Access by index -> [0], [-1], ...
tuple use (), no method, access by index -> [0], [-1], ...
dictionary use {}, have method like: keys, values, items, get, pop, ... Access by key -> ['name'], ['price'], ...
set use {}, but no key-value pairs, have method like: add, remove, pop, ... No access by index or key, only by iteration
"""

# exercise:
"""
Create a list of 3 product names and add a 4th using .append()
Create a tuple of 3 allowed currencies: USD, VND, EUR
Create a dict for one product with keys: name, price, category  — then update the price and add a new key discount with value 0.1
Create a set of tags: "sale", "new", "sale", "featured" — print it and observe the duplicate
"""

products = ['laptop', 'mouse', 'keyboard']
products.append('monitor')

currencies = ("USD", "VND", "EUR")

product = {
    "name": "laptop",
    "price": 999,
    "category": "electronics"
}
product["price"] = 899
product["discount"] = 0.1

tags = {"sale", "new", "sale", "featured"}
print(tags)

print(products)
print(currencies)
print(product)