# Basic structure
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")

# Catch multiple specific errors
try:
    value = int("abc")
except ValueError:
    print("That's not a number")
except TypeError:
    print("Wrong type entirely")

# Catch any error (use sparingly)
try:
    something_risky()
except Exception as e:
    print(f"Something went wrong: {e}")

# finally — always runs, even if there's an error
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Done attempting to read file")