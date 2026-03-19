# Topic 1 — Classes, Objects, __init__, self
# Learning goal: understand how to define a class and create objects


class Customer:
    def __init__(self, name, email, is_active=True):
        self.name = name
        self.email = email
        self.is_active = is_active

    def profile(self):
        status = "Active" if self.is_active else "Inactive"
        print(f"Name: {self.name} \nEmail: {self.email} \nStatus: {status}")
        print("-" * 20)

customer1 = Customer("John","john@example.com", True)
customer2 = Customer("Alice","alice@example.com", False)

customer1.profile()
customer2.profile()