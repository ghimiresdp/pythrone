"""
! Simple unit testing with `assert` keyword

* The `assert` keyword is used to check for the truthfulness or equality of the
  given expression
* It is a python's reserved keyword.
"""


def multiply_divide(number):
    if number % 2 == 0:
        return int(number / 2)
    return number * 2


def test():
    assert multiply_divide(4) == 2

    assert multiply_divide(4) == 8  # AssertionError
    """NOTE: if we uncomment the above line, we get an `AssertionError`.
    Assertion error occurs when we do not get expected result.

    The test below was intentionally checked for the equality of 1 + 2 == 4
    so that we would get `AssertionError`
    """


if __name__ == "__main__":
    test()
