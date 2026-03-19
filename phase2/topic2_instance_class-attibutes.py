class Product:
    # Class attribute
    currency = "VND"
    total_products = 0
    
    def __init__(self, name, price):
        # Instance attributes - specific to each product
        self.name = name
        self.price = price
        Product.total_products += 1
        
laptop = Product("Laptop", 999.0)
mouse = Product("Mouse", 49.0)

print(laptop.currency) # Access class attribute via instance -> VND
print(mouse.currency) # Access class attribute via instance -> VND
print(Product.currency) # Access class attribute via class -> VND
print(laptop.name) # Access instance attribute -> Laptop
print(mouse.name) # Access instance attribute -> Mouse

## IN Odoo:

class SaleOrder(models.Model):
    _name = "sale.order" # class attribute
    _description = "Sales Order" # class attribute
    
    name = fields.Char()