### Type Annotations in Python 3

Type annotations in Python 3 allow you to specify the expected data types of variables and function arguments. This doesn't enforce type checking at runtime but provides a way to document your code and helps tools like **mypy** to perform static type checking.

#### Basic Syntax

1. **Variable Annotations**:

   ```python
   age: int = 25
   name: str = "Alice"
   height: float = 5.9
   ```

   Here, `age` is expected to be an integer, `name` a string, and `height` a float.

2. **Function Annotations**:
   You can annotate function arguments and return types.

   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}!"
   ```

   This function expects a string `name` and returns a string.

3. **Complex Types**:
   For lists, dictionaries, and other container types, use the `typing` module.

   ```python
   from typing import List, Dict

   numbers: List[int] = [1, 2, 3]
   user_data: Dict[str, int] = {"age": 30, "height": 170}
   ```

### Function Signatures and Variable Types

Type annotations improve the readability and maintainability of your code by clearly indicating what types are expected. They are particularly useful in function signatures.

#### Example

```python
from typing import List, Tuple

def calculate_average(grades: List[int]) -> float:
    return sum(grades) / len(grades)

def get_student_info() -> Tuple[str, int]:
    return ("Alice", 20)
```

Here, `calculate_average` expects a list of integers and returns a float. `get_student_info` returns a tuple containing a string and an integer.

### Duck Typing

Duck typing is a concept related to dynamic typing in Python. It means that the type or class of an object is less important than the methods it defines or the operations it supports. The name comes from the saying, "If it looks like a duck and quacks like a duck, it must be a duck."

In Python, you don't check the type of an object to determine if it can be used in a particular way; instead, you check whether it supports the operations you want to perform.

#### Example

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_quack(duck_like):
    duck_like.quack()

duck = Duck()
person = Person()

make_quack(duck)  # Outputs: Quack!
make_quack(person)  # Outputs: I'm quacking like a duck!
```

Both `Duck` and `Person` can be passed to `make_quack` because they both have a `quack` method, even though they are not of the same type.

### Validating Code with `mypy`

`mypy` is a static type checker for Python that checks type annotations without executing the code. It helps catch potential type errors and ensures that your annotations are being used correctly.

#### Installation

You can install `mypy` via pip:

```bash
pip install mypy
```

#### Using `mypy`

To check a Python file for type errors:

```bash
mypy your_file.py
```

#### Example

Consider the following code with type annotations:

```python
# student.py

from typing import List

def get_first_name(full_name: str) -> str:
    return full_name.split()[0]

def calculate_mean(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)

age: int = "25"  # This is an error: assigning a string to an int variable
```

When you run `mypy`:

```bash
mypy student.py
```

You might get an error:

```
student.py:10: error: Incompatible types in assignment (expression has type "str", variable has type "int")
```

### Summary

- **Type Annotations**: Provide a way to specify expected types for variables and function parameters/return values.
- **Duck Typing**: Focuses on the presence of methods and properties rather than the actual type of an object.
- **mypy**: A tool to check the correctness of type annotations in Python code, catching potential type-related issues.

### Practical Example

Let's put this all together with a practical example.

```python
# types_example.py

from typing import List, Dict, Tuple

# Define a function with type annotations
def add_numbers(a: int, b: int) -> int:
    return a + b

# Using type annotations for variables
name: str = "Bob"
age: int = 30
scores: List[int] = [85, 90, 95]
user_info: Dict[str, str] = {"username": "bob123", "email": "bob@example.com"}

# Function to demonstrate duck typing
def make_quack(duck_like):
    duck_like.quack()

# Class examples
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

# Validating with mypy
def validate_data(data: Tuple[int, str]) -> None:
    number, text = data
    print(f"Number: {number}, Text: {text}")

# Sample usage
duck = Duck()
person = Person()

make_quack(duck)  # Outputs: Quack!
make_quack(person)  # Outputs: I'm quacking like a duck!

validate_data((10, "Sample"))  # Outputs: Number: 10, Text: Sample
```

### Next Steps

1. **Run `mypy`** on the above example to see how it catches type errors.
2. **Practice** using type annotations and `mypy` in your own code.
3. **Explore** advanced typing concepts like generics, type aliases, and union types.
