import json

# dict -> JSON string(serializing)
# product = {"name": "Laptop", "price": 999, "available": True}
# json_string = json.dumps(product)
# # print(json_string)

# # # pretty print
# # print(json.dumps(product, indent=2))

# #JSON string -> dict (deserializing)

# data = '{"name": "Mouse", "price": 49}'
# product = json.loads(data)
# # print(product["name"])
# # print(product)

# #read json from file
# with open("products.json", "r") as f:
#     data = json.load(f)
    
# print(data)

# # write JSON from file
# with open("product.json", "w") as f:
#     json.dump(product, f , indent=2)
    
"""
four methods to remember
json.dumps() - dict to string
json.loads() - string to dict
json.dump() - dict to file
json.load() - file to dict

Write a script that:

1. Creates a list of 3 product dicts with `name`, `price`, `available`
2. Writes them to a file called `products.json` using `json.dump()`
3. Reads the file back using `json.load()`
4. Loops through and prints only **available** products in this format:
```
Laptop - $999.00
Keyboard - $79.00

"""

products =[{"name": "laptop", "price": 499, "available":True}, {"name": "mouse", "price": 99, "available":False},{"name": "monitor", "price": 199, "available":True},]

with open("products.json", "w") as f:
    json.dump(products, f)

with open("products.json", "r") as f:
    data = json.load(f)
    
for d in data:
    if d["available"]:
        print(f"{d['name']} - ${d['price']}")
