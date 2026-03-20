## Dunder method (double underscore method) are special methods in Python call automatically in certain situations

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        # called when you print() the object
        return f"Product: {self.name} | Price: {self.price}"
    
    def __repr__(self):
        # called in the console/debbugger, should be unambiguous
        return f"Product(name={self.name}, price={self.price})"
    
    def __len__(self):
        # called when you do len(object)
        return len(self.name)
    
    def __eq__(self, other):
        # called when you do product1 == product2
        return self.price == other.price
    
    
p1 = Product("Laptop", 999.0)
p2 = Product("Laptop Pro", 1299.0)

print(p1)
print(repr(p1))
print(len(p1))
print(p1 == p2)