# Chapter 21.2: Testing using `unittest` module

**Table of contents**:
- [Chapter 21.2: Testing using `unittest` module](#chapter-212-testing-using-unittest-module)
  - [Introduction to `unittest`](#introduction-to-unittest)
    - [Example of unittest](#example-of-unittest)
  - [`setUp` and `tearDown` methods](#setup-and-teardown-methods)



## Introduction to `unittest`

The `unittest` module is a python's builtin test module. It contains all basics
of software testing, example: test discovery,assertion, setup/teardown, etc.

As python is an Object-oriented programming language, it's `unittest` module
also implements Class-based interface to setup the test module. We can easily
import `unittest` module to start testing our software.

### Example of unittest

The following is a basic example of a testcase which will test for the
correctness of the given function, "reverse_word".

```python
import unittest

def reverse_word(word: str):
    return word[::-1]

class TestReverseWord(unittest.TestCase):
    def test_reverse():
        self.assertEqual(reverse_word("abcde"), "edcba")


if __name__ == "__main__":
    main()
```

## `setUp` and `tearDown` methods

A setup method is a method that runs before each test. The `setUp` method
generally initializes values before testcases are run. For example, If we need
an authorization token to test an API, we can get them in the `setUp` method.

A `tearDown` method is a method that runs after each test. This method is used
as a cleanup method after test gets executed.

An example of setup and teardowm methods are as follows:
```python
def celsius_to_fahrenheit(celsius: float):
    return (9 / 5) * celsius + 32


class TestTemperatureChange(TestCase):
    def setUp(self) -> None:
        # This method runs before each test case inside of this test class
        self.celsius = 37

    def tearDown(self) -> None:
        # This method runs after each test case inside of this test class
        del self.celsius

    def test_conversion_from_setup(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(self.celsius), 98.6)

```
