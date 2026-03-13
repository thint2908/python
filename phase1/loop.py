#loop

products = ["laptop", "phone", "tablet"]

# for - use when you know what you are looping over
for product in products:
    print(product)
    
# while - use when you loop until a condition is met
count = 0
while count < 3:
    print("checking...")
    count += 1
    
# loop with enumerate - use when you need the index of the item in the loop

for index, product in enumerate(products):
    print(f"{index + 1}. {product}")
    
def ex():
    products = [
        {"name": "laptop", "price": 999},
        {"name": "phone", "price": 499},
        {"name": "tablet", "price": 299},
    ]
    
    for product in products:
        label = " ★ Premium" if product["price"] > 500 else ""
        if product["price"] > 500:
            print(f"{product['name']} {label}")
        else:
            print(f"{product['name']}")
            
ex()