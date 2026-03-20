class SaleOrder:
    def __init__(self, other_id, customer_name, items):
        self.other_id = other_id
        self.customer_name = customer_name
        self.items = items
        
    def __str__(self):
        return f"Order #{self.other_id} for {self.customer_name}"
    
    def __len__(self):
        return len(self.items)
    
    @property
    def total(self):
        return sum(item['price'] for item in self.items)
    
    def summary(self):
        return f"Order #{self.other_id} for {self.customer_name} \nItems: {len(self)} \nTotal: {self.total:.2f}"
    
order1 = SaleOrder(123, "Alice", [
    {"name": "Widget", "price": 10.0},
    {"name": "Gadget", "price": 15.0}
])  

order2 = SaleOrder(124, "Bob", [
    {"name": "Widget", "price": 10.0},
    {"name": "Gadget", "price": 15.0}
])  

order3 = SaleOrder(125, "Charlie", [
    {"name": "Widget", "price": 10.0},
    {"name": "Gadget", "price": 15.0}
])

print(order1.summary())
print(order2.summary())
print(order3.summary())