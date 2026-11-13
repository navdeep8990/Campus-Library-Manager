# main.py
from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, 42)
dvd = DVD("Planet Earth", 3, 120)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 0. LibraryItem is abstract and cannot be created directly
print("=== Abstract class ===")
try:
    LibraryItem("x", 1)
except TypeError as e:
    print("Cannot create LibraryItem:", e)

# 1. Borrowing with error handling
print("\n=== Borrowing ===")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Trigger the borrow-limit error and the not-borrowed error, catching each
print("\n=== Borrow limit ===")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

print("\n=== Returning ===")
try:
    bob.return_item(book)  # should fail: Bob never borrowed the book
except ValueError as e:
    print("Could not return:", e)

try:
    fee = alice.return_item(book, days_late=3)
    print(f"Alice returned '{book.title}' 3 days late. Fee: Rs {fee}")
except ValueError as e:
    print("Could not return:", e)

print("Alice's borrowed titles:", alice.borrowed_titles())
print("Bob's borrowed titles:", bob.borrowed_titles())

# 3. Polymorphism: one loop, no type checks
print("\n=== Polymorphism ===")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("\n=== Class attribute ===")
print("Total items created:", Book.total_items)

# 5. Encapsulation: private attribute cannot be read from outside
print("\n=== Encapsulation ===")
try:
    print(magazine.__available)
except AttributeError as e:
    print("AttributeError:", e)
print(f"Is '{magazine.title}' available? {magazine.is_available()}")
print(f"Is '{book.title}' available? {book.is_available()}")
