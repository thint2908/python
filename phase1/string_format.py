name = "Laptop"
price = 999.5
quantity = 10

# f-string (modern, preferred)
print(f"{name} costs {price}")

# Format numbers inside f-strings

print(f"Price: {price:.2f}")
print(f"Quantity: {quantity:04d}")

# usefull string method
name.upper()
name.lower()
name.strip() # remove whitespace from both ends
name.replace("L", "l")


# check content
"lap" in name # -> True
name.startswith("Lap") # -> True
name.split(" ") # split into a list by space

"""
Write a function called `format_product_label` that takes `name`, `price`, and `discount` (a float like `0.1` meaning 10%) and prints:
```
LAPTOP
Original Price : 999.50
Discount       : 10%
Final Price    : 899.55
"""

def format_product_label(name, price, discount):
    final_price = price * (1 - discount)
    print(f"{name.upper()}")
    print(f"Original Price : {price:.2f}")
    print(f"Discount       : {discount*100:.0f}%")
    print(f"Final Price    : {final_price:.2f}")
    
format_product_label("Laptop", 999.50, 0.1)