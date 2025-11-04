"""
==================================================
File: 1_mutable_defaults.py
Topic: Understanding Mutable Default Arguments in Python
==================================================

When a mutable object (like a list or dict) is used as a default
argument, it can lead to unexpected behavior because the object is
created only once when the function is defined — not each time it is called.
"""

#  Problem Example: Shared mutable default
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print("Problem Example:")
print(add_item("apple"))     # ['apple']
print(add_item("banana"))    # ['apple', 'banana']  <-- unexpected shared list

#  Correct Fix using None
def add_item_safe(item, basket=None):
    if basket is None:
        basket = []  # new list each call
    basket.append(item)
    return basket

print("\nFixed Version:")
print(add_item_safe("apple"))     # ['apple']
print(add_item_safe("banana"))    # ['banana']

#  Verify shared object IDs in buggy version
def buggy(basket=[]):
    print(f"Memory ID of basket: {id(basket)}")
    basket.append("x")
    return basket

print("\nMemory IDs showing reuse of same list:")
buggy()
buggy()  # Same ID → same object
