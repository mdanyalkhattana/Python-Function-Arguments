"""
==================================================
File: 3_type_checking_and_practice.py
Topic: Type Checking and Function Practice
==================================================
"""

# Using isinstance() for dynamic type handling
def operate(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sum(data.values())
    elif isinstance(data, set):
        return len(data)
    else:
        return "Unsupported type"

print("Operate Function Results:")
print(operate([1, 2, 3]))          # 6
print(operate({'a': 1, 'b': 2}))   # 3
print(operate({10, 20}))           # 2


# Function to describe multiple types
def describe_types(*args):
    print("\nDescribing Argument Types:")
    for arg in args:
        print(f"{arg} → {type(arg)}")

describe_types(10, [1, 2], {'a': 1}, (4, 5), {9, 10})


# Practice: Summarize List
def summarize_list(lst):
    return {
        "sum": sum(lst),
        "average": sum(lst) / len(lst),
        "length": len(lst)
    }

print("\nSummarizing a list:")
nums = [10, 20, 30]
print(summarize_list(nums))


# Practice Challenge: Smart Calculator
def smart_calculator(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Invalid operation"

print("\nSmart Calculator:")
print("Sum:", smart_calculator(2, 3, 4))
print("Product:", smart_calculator(2, 3, 4, operation="multiply"))
