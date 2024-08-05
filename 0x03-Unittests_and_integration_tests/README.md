### New Concepts Breakdown

#### 1. `unittest` — Unit Testing Framework

The `unittest` module is Python's built-in library for creating and running unit tests. Unit tests are tests that cover the smallest parts of an application, usually individual functions or methods.

**Example:**

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

#### 2. `unittest.mock` — Mock Object Library

The `unittest.mock` module provides a way to create mock objects for testing. Mock objects simulate the behavior of real objects in a controlled way.

**Example:**

```python
from unittest.mock import Mock

# Creating a mock object
mock = Mock()
mock.method.return_value = 'result'

print(mock.method())  # Output: result
```

#### 3. How to Mock a Readonly Property with Mock?

You can use the `property` decorator to mock a readonly property.

**Example:**

```python
from unittest.mock import patch

class MyClass:
    @property
    def readonly_property(self):
        return 'original value'

with patch.object(MyClass, 'readonly_property', new_callable=Mock) as mock_property:
    mock_property.return_value = 'mocked value'
    obj = MyClass()
    print(obj.readonly_property)  # Output: mocked value
```

#### 4. `parameterized`

The `parameterized` library allows you to run a test multiple times with different inputs.

**Example:**

```python
from parameterized import parameterized
import unittest

class TestParameterized(unittest.TestCase):
    @parameterized.expand([
        ("test1", 1, 2, 3),
        ("test2", 4, 5, 9),
    ])
    def test_add(self, name, a, b, expected):
        self.assertEqual(a + b, expected)

if __name__ == '__main__':
    unittest.main()
```

#### 5. Memoization

Memoization is a technique to optimize functions by caching the results of expensive function calls and reusing them when the same inputs occur again.

**Example:**

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expensive_function(x):
    # Simulate an expensive computation
    return x * x

print(expensive_function(4))  # First call, computes the result
print(expensive_function(4))  # Second call, returns cached result
```

### The Difference Between Unit and Integration Tests

- **Unit Tests:** Test individual components or functions in isolation. They are fast and help catch bugs early in the development cycle.
- **Integration Tests:** Test the interactions between different components or systems. They ensure that integrated parts work together as expected.

### Common Testing Patterns

- **Mocking:** Using mock objects to simulate the behavior of real objects.
- **Parametrization:** Running the same test with different inputs.
- **Fixtures:** Setting up the environment for tests. Fixtures are reusable components that provide a known state for tests to run.

**Example of a Fixture:**

```python
import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        self.value = 10

    def test_example(self):
        self.assertEqual(self.value, 10)

    def tearDown(self):
        self.value = None

if __name__ == '__main__':
    unittest.main()
```
