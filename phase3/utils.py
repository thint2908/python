"""
🏋️ Exercise
Create two files in your phase3-intermediate/ folder:
utils.py — contains:

A function format_currency(amount, symbol="$") that returns "$1,234.50"
A function slugify(text) that returns text lowercased with spaces replaced by - (e.g. "Sale Order" → "sale-order")
"""


def format_currency(amount, symbol='$'):
    return f"{symbol}{amount:,.2f}"

def slugify(text):
    return text.lower().replace(" ", "-")

