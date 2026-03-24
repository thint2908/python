# in odoo every file is a module, every folder is a package. 

import math
print(math.sqrt(16))  # using a function from the math module
print(math.pi)

# import specific things from a module
from math import sqrt, pi
print(sqrt(25))
print(pi)

# import with alias
import datetime as dt
today = dt.date.today()
print(today)

# import your own file
# if you have utils.py in the same folder:
# from utils import some_function

# my_module/
# ├── __init__.py
# ├── models.py
# └── utils.py

# from my_module.model import Product
# from my_module.utils import format_price

from utils import format_currency, slugify

print(format_currency(1234.5))
print(format_currency(99.9, "₫"))
print(slugify("Sale Order"))
print(slugify("Product Template"))