
from datetime import date, datetime, timedelta

# Today date
today = date.today()
print("Today's date:", today)

# current date and time
now = datetime.now()
print("Current date and time:", now)

# create a specific date
d = date(2026,1,1)
print("Specific date:", d)

# formatting - date to string
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%B %d, %Y"))

# parsing - string to date
dString = datetime.strptime("24/03/2026", "%d/%m/%Y")
print("Parsed date:", dString)

# Arithmetic with timedelta
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
due_date = today + timedelta(days=30)
print("Tomorrow:", tomorrow)
print("Next week:", next_week)
print("Due date:", due_date)

# difference between two dates
delta = due_date - today
print("Days until due date:", delta.days)

def invoice_info(invoice_date_str, due_days):
    invoice_date = datetime.strptime(invoice_date_str, "%d/%m/%Y")
    due_date = invoice_date + timedelta(days=due_days)
    days_remaining = (due_date - datetime.now()).days
    overdue = datetime.now() > due_date
    return {
        "invoice_date": invoice_date.strftime("%d/%m/%Y"),
        "due_date": due_date.strftime("%d/%m/%Y"),
        "days_remaining": days_remaining,
        "overdue": overdue
    }
    
print(invoice_info("01/09/2024", 30))
print(invoice_info("01/08/2026", 30))