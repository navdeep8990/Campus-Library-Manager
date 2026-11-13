# main.py
from models import LibraryItem, Book, Magazine, DVD, Member

# ---------------------------------------------------------------
# Step 2 checkpoint: LibraryItem is abstract
# ---------------------------------------------------------------
print("=== Step 2: LibraryItem is abstract ===")
try:
    LibraryItem("x", 1)
except TypeError as e:
    print("TypeError:", e)

# ---------------------------------------------------------------
# Step 3 checkpoint: describe() and total_items going up
# ---------------------------------------------------------------
print("\n=== Step 3: Child classes and total_items ===")
print("Total items at start:", LibraryItem.total_items)

book = Book("Python 101", 1, "A. Rao")
print(book.describe(), "| total_items:", LibraryItem.total_items)

magazine = Magazine("Tech Monthly", 2, 42)
print(magazine.describe(), "| total_items:", LibraryItem.total_items)

dvd = DVD("Planet Earth", 3, 120)
print(dvd.describe(), "| total_items:", LibraryItem.total_items)

extra_book = Book("Clean Code", 4, "R. Martin")  # used to test the 4th-item limit
print(extra_book.describe(), "| total_items:", LibraryItem.total_items)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# ---------------------------------------------------------------
# Step 4 + Step 5: Member, borrowing and error handling
# ---------------------------------------------------------------
print("\n=== Step 4/5: Borrowing with error handling ===")

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Trigger the borrow-limit error and the not-borrowed error, catching each

# Same item twice
try:
    alice.borrow(book)  # should fail: Alice already has this book
except ValueError as e:
    print("Could not borrow:", e)

# 4th item (Alice's default limit is 3)
try:
    alice.borrow(magazine)
    print("Alice borrowed:", magazine.describe())
    alice.borrow(dvd)
    print("Alice borrowed:", dvd.describe())
    alice.borrow(extra_book)  # should fail: this would be her 4th item
except ValueError as e:
    print("Could not borrow:", e)

# Bob's limit is 1
try:
    bob.borrow(extra_book)
    print("Bob borrowed:", extra_book.describe())
    alice.return_item(dvd)
    print("Alice returned:", dvd.describe())
    bob.borrow(dvd)  # should fail: this would be Bob's 2nd item
except ValueError as e:
    print("Could not borrow:", e)

# Returning something not borrowed
try:
    bob.return_item(book)  # should fail: Bob never borrowed the book
except ValueError as e:
    print("Could not return:", e)

# Successful return with a late fee
try:
    fee = alice.return_item(book, days_late=3)
    print(f"Alice returned '{book.title}' 3 days late. Fee: Rs {fee}")
except ValueError as e:
    print("Could not return:", e)

print("Alice's borrowed titles:", alice.borrowed_titles())
print("Bob's borrowed titles:", bob.borrowed_titles())

# ---------------------------------------------------------------
# Step 5 checkpoint: polymorphism
# ---------------------------------------------------------------
print("\n=== Step 5: Polymorphism ===")

# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)

# ---------------------------------------------------------------
# Step 6: encapsulation
# ---------------------------------------------------------------
print("\n=== Step 6: Encapsulation ===")
try:
    print(magazine.__available)
except AttributeError as e:
    print("AttributeError:", e)
print(f"Is '{magazine.title}' available? {magazine.is_available()}")
print(f"Is '{book.title}' available? {book.is_available()}")
