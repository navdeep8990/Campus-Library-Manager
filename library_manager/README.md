# Campus Library Manager

Run with Python 3.12 or later (no external packages):

```
python3 main.py
```

The full console output of the final run is in `output.txt`.

## Reflection

**1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?**

`LibraryItem` is abstract because a generic "library item" has no real late-fee rule; it only exists to hold the shared behaviour (title, ID, availability) and to force every child class to define its own `late_fee()`. Because `late_fee()` is marked with `@abstractmethod`, Python refuses to create an object of any class that has not implemented it. If `DVD` forgot to write `late_fee()`, then `DVD("Planet Earth", 3, 120)` would raise a `TypeError` as soon as we tried to create it, so the mistake is caught immediately instead of later at runtime.

**2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?**

Reading `item.__available` from outside the class raises an `AttributeError`, because Python name-mangles attributes that start with two underscores (it is stored internally as `_LibraryItem__available`). We use `is_available()` because it gives read-only access to the state, while only `mark_borrowed()` and `mark_returned()` are allowed to change it. This encapsulation keeps the item's availability consistent and stops outside code from setting it to a wrong value by accident.

**3. What is the difference between `LibraryItem.total_items` and `self.title`?**

`LibraryItem.total_items` is a class attribute: there is only one copy, shared by every item, and it counts how many items have been created (it is 3 in the demo). `self.title` is an instance attribute: each object has its own separate value, such as "Python 101" for the book and "Planet Earth" for the DVD. Changing one object's title does not affect any other object, but updating `total_items` changes the value seen by all of them.
