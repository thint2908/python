# TOPIC 4: Inheritance

# Inheritance lets one class borrow everything from another and extend it.

""" 
class SaleOrder(models.Model):   # SaleOrder inherits from models.Model
class ResPartner(models.Model):  # ResPartner inherits from models.Model
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Some sound"
    

class Dog(Animal): # Dog inherits from Animal
    def speak(self):
        return "Woof!"
    
class Cat(Animal): # Cat inherits from Animal
    def speak(self):
        return "Meow!"
    
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())


# super() when the child class needs to extend the parent's __init__ rather than replace it

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def introduce(self):
        return f"Hi, I am {self.name}"

class Customer(Person):
    def __init__(self, name, email, membership_level="Gold"):
        super().__init__(name, email) # call the parent's __init__ to set name and email
        self.membership_level = membership_level

    def introduce(self):
        return super().introduce() + f" - {self.membership_level} member"
    
class Employee(Person):
    def __init__(self, name, email, department, salary):
        super().__init__(name, email)
        self.department = department
        self.salary = salary

    def work_info(self):
        return f" Dept: {self.department} | Salary: {self.salary:,.2f}"
    
customer = Customer("Alice", "alice@example.com", "Platinum")
employee = Employee("Bob", "bob@example.com", "Marketing", 50000)

print(customer.introduce())
print(employee.work_info())