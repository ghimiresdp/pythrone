"""
! Simple unit testing with `assert` keyword

* The `assert` keyword is used to check for the truthfulness or equality of the
  given expression
* It is a python's reserved keyword.
"""


def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3

    # assert add(1, 2) == 4
    """NOTE: if we uncomment the above line, we get an `AssertionError`.
    Assertion error occurs when we do not get expected result.

    The test below was intentionally checked for the equality of 1 + 2 == 4
    so that we would get `AssertionError`
    """


test_add()
