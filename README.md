 
# 🐍 Python Function Arguments — Beginner to Advanced Guide

A comprehensive beginner-friendly guide explaining how **Python handles function arguments** — from basics to advanced topics like `*args`, `**kwargs`, and safe coding practices.

---

## 📘 Table of Contents

1. [Introduction](#introduction)
2. [Mutable Default Arguments](#1-mutable-default-arguments)
3. [`*args` — Variable Positional Arguments](#2-args--variable-positional-arguments)
4. [`**kwargs` — Variable Keyword Arguments](#3-kwargs--variable-keyword-arguments)
5. [Keyword-Only Arguments (`*` usage)](#4-keyword-only-arguments)
6. [Type Checking Inside Functions](#5-type-checking-inside-functions)
7. [Practice Exercises](#6-practice-exercises)
8. [Summary Table](#7-summary-table)
9. [License](#license)

---

## 🧠 Introduction

In Python, functions are flexible — you can define them with fixed parameters, optional ones, or even dynamically accept **any number of arguments**.
But this flexibility can cause confusion and subtle bugs if not understood properly.

This guide walks you step-by-step through all important argument concepts — using simple explanations, visuals, and examples.

---

## 1️⃣ Mutable Default Arguments

### ❌ The Common Bug

```python
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))    # ['apple']
print(add_item("banana"))   # ['apple', 'banana'] ❌ Unexpected!
```

🧩 Problem:
Python evaluates default arguments **once** at function definition time — not every call.
So the same list `[]` is reused across calls!

---

### ✅ The Correct Fix

```python
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
```

Output:

```python
print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana']
```

---

### 💡 Why It Works

`None` is immutable — so it’s safe as a default.
Each call creates a **new list** only when needed.

---

## 2️⃣ `*args` — Variable Positional Arguments

Used to pass a **variable number of positional arguments** to a function.

```python
def sum_all(*args):
    return sum(args)
```

🧪 Example:

```python
print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
```

Inside the function,
`args` → is a **tuple** containing all positional arguments.

---

### 🧩 Another Example

```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")
```

Output:

```
Hello, Ali!
Hello, Sara!
Hello, John!
```

---

## 3️⃣ `**kwargs` — Variable Keyword Arguments

Used to collect all **named arguments** into a dictionary.

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
```

🧪 Example:

```python
show_info(name="Danyal", age=21, country="Pakistan")
```

Output:

```
name = Danyal
age = 21
country = Pakistan
```

Inside the function:
`kwargs` → is a **dict** of key–value pairs.

---

### 🧩 Combining `*args` and `**kwargs`

```python
def smart_printer(*args, **kwargs):
    total = sum(a for a in args if isinstance(a, (int, float)))
    text = " ".join(str(v) for v in kwargs.values() if isinstance(v, str))
    print(f"Sum of numbers: {total}")
    print(f"Joined strings: {text}")
```

Call:

```python
smart_printer(1, 2, 3, name="Danyal", job="Developer")
```

Output:

```
Sum of numbers: 6
Joined strings: Danyal Developer
```

---

## 4️⃣ Keyword-Only Arguments

Using `*` forces the next parameters to be passed **only by name**.

```python
def configure(*, mode="dark", verbose=False):
    print(mode, verbose)
```

Call:

```python
configure(mode="light", verbose=True)  # ✅ Works
configure("light")                     # ❌ TypeError
```

💡 This is useful to make your function calls **clearer and less error-prone**.

---

## 5️⃣ Type Checking Inside Functions

You can check data types dynamically using `isinstance()`:

```python
def operate(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sum(data.values())
    elif isinstance(data, set):
        return len(data)
```

🧪 Example:

```python
print(operate([1,2,3]))           # 6
print(operate({'a':1,'b':2}))     # 3
print(operate({9,10}))            # 2
```

✅ `isinstance()` helps you write **safe, type-aware code**.

---

## 6️⃣ Practice Exercises

1. **Fix Mutable Default Bug**

   ```python
   def add_item(item, basket=[]):
       basket.append(item)
       return basket
   # Fix using None
   ```

2. **Describe All Argument Types**

   ```python
   def describe_types(*args):
       for arg in args:
           print(f"{arg} → {type(arg)}")
   ```

3. **Summarize List**

   ```python
   def summarize_list(lst):
       return sum(lst), sum(lst)/len(lst), len(lst)
   ```

4. **Smart Printer**

   ```python
   def smart_printer(*args, **kwargs):
       total = sum(args)
       text = " ".join(str(v) for v in kwargs.values())
       return total, text
   ```

---

## 7️⃣ Summary Table

| Symbol      | Type                | Description                     | Stored As |
| ----------- | ------------------- | ------------------------------- | --------- |
| `arg`       | Positional          | Normal argument                 | Variable  |
| `arg=value` | Default             | Optional argument               | Variable  |
| `*args`     | Variable positional | Any number of unnamed arguments | Tuple     |
| `**kwargs`  | Variable keyword    | Any number of named arguments   | Dict      |
| `*`         | Separator           | Enforces keyword-only args      | —         |

---

## 🧩 Example Mini Project

```python
def summarize_list(lst):
    return {
        "sum": sum(lst),
        "average": sum(lst)/len(lst),
        "length": len(lst)
    }

nums = [10, 20, 30]
print(summarize_list(nums))
```

Output:

```
{'sum': 60, 'average': 20.0, 'length': 3}
```

---

## 📜 License

This educational content is free to use for learning, teaching, or project documentation.
© 2025 M Danyal — All rights reserved.

 
