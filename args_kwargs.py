"""
==================================================
File: 2_args_kwargs.py
Topic: Variable Arguments in Python (*args and **kwargs)
==================================================
"""

# *args example → collects multiple positional arguments into a tuple
def sum_all(*args):
    print(f"args as tuple: {args}")
    return sum(args)

print("Sum using *args:")
print(sum_all(1, 2, 3, 4))   # 10


# **kwargs example → collects named keyword arguments into a dictionary
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print("\nInformation using **kwargs:")
show_info(name="Danyal", age=21, country="Pakistan")


# Combine *args and **kwargs
def smart_printer(*args, **kwargs):
    total = sum(a for a in args if isinstance(a, (int, float)))
    text = " ".join(str(v) for v in kwargs.values() if isinstance(v, str))
    print(f"Sum of numeric args: {total}")
    print(f"Joined strings from kwargs: {text}")

print("\nUsing both *args and **kwargs:")
smart_printer(10, 20, name="Ali", job="Developer")


# Keyword-only arguments using *
def configure(*, mode="dark", verbose=False):
    print(f"Mode: {mode}, Verbose: {verbose}")

print("\nKeyword-only argument example:")
configure(mode="light", verbose=True)

# Practice: custom function with args and kwargs
def combine_examples(*args, **kwargs):
    print("\nAll positional arguments (args):", args)
    print("All keyword arguments (kwargs):", kwargs)
    print("Sum of all numbers:", sum(a for a in args if isinstance(a, (int, float))))
    print("Keys passed as kwargs:", list(kwargs.keys()))

combine_examples(1, 5, 9, language="Python", version=3.13)
