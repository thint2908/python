# Writing a file

with open("products.txt", "w") as f:
    f.write("Laptop, 999,True\n")
    f.write("Mouse,49,True\n")


# Reading a file
with open("products.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line (more practical):
with open("products.txt", "r") as f:
    for line in f:
        print(line.strip()) # strip() to remove \n at end of each line
        
"""
The `with` keyword handle opening and closing the file automatically - always use it, never use `open()` without `with`

MODE:
- "r" - read (default)
- "w" - write (overwrite)
- "a" - append (add to end of file)
- "x" - create a new file, fail if file already exists

### 🏋️ Exercise

Write a script that:

1. Writes a file called `products.txt` with at least 3 products, one per line, in this format: `name,price,quantity`
2. Reads the file back line by line
3. For each line, **split by comma**, parse the values, and print:
```
Product: Laptop | Price: 999.0 | Qty: 5
"""

def ex():
    with open("products.txt", "w") as f:
        f.write("Laptop,999.0,5\n")
        f.write("Mouse,49.0,10\n")
        f.write("Keyboard,79.0,3\n")

    with open("products.txt", "r") as f:
        for line in f:
            name, price, quantity = line.strip().split(",")
            print(f"Product: {name} | Price: {float(price)} | Qty: {int(quantity)}")
            
ex()