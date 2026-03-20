## PROPERTY lets you access a method like an attribute - no parentheses needed. Use it for computed values that depend on other attributes.

class Product:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        
    @property
    def total_value(self):
        return self.price * self.quantity
    
p = Product(5, 20.0)
print(p.total_value)