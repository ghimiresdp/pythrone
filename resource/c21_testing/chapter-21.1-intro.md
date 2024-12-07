# Chapter 21.1: Introduction to Software Testing

**Table of contents**:
- [Chapter 21.1: Introduction to Software Testing](#chapter-211-introduction-to-software-testing)
  - [Software Testing and its purpose](#software-testing-and-its-purpose)
    - [The `assert` keyword](#the-assert-keyword)
    - [Types of testing](#types-of-testing)
  - [Testing Approaches](#testing-approaches)
    - [Black-box testing](#black-box-testing)
    - [White-box testing](#white-box-testing)
    - [Grey-box testing](#grey-box-testing)


## Software Testing and its purpose

Software testing is an approach to test our own software by adding some cases
that would check whether our code works properly on all possible conditions.

We use Software testing to check whether:
- The code block works as expected
- The code gives proper exception as expected when something unacceptable occurs
- The code is resilient and robust enough to handle high traffic (`Scalable`)
- The new update in our code modifies previous expected behaviors (`Regression`)

Let us take an example of a function which takes a number and divides it by 2 if
it is an even and multiplies by 2 if it is 2.

```python
def multiply_divide(number):
    if number%2==0:
        return int(number/2)
    return number * 2
```

for the above code snippet, we can check the following:

1. try some even number and see if it results in half of the provided number.
2. try some odd number and see if it results in double of the provided one.
3. check if it handles exception if it is fed with wrong data type.

### The `assert` keyword

In python, assert keyword plays a vital role in testing the code snippet. If the
condition is met or `True` in the `assert` statement, then the code will run
otherwise, `Assertion Error` will be raised.

Example:
```python
assert multiply_divide(4)==2    # code continues to run
assert multiply_divide(4)==8    # AssertionError

```

### Types of testing

Tests can be classified into different types based on its category.

1. **Functional**: used to check the code snippets
   - `Unit testing`: testing specific function or a part of a code
   - `Integration testing`: testing whether different parts of a code integrates with each other
   - `System testing`: testing whether the system works properly and as expected
   - `Acceptance testing`: testing whether the solution is acceptable to clients

2. **Non-Functional**: used to check the software behavior
   - `Performance testing`: used to check if the solution is optimum
   - `Scalability testing`: used to check if the solution is scalable
   - `Reliability testing`: used to check if the solution is reliable
   - `Security testing`: used to check if the solution is secure

3. **Maintenance**: used to test if new update behavior
   - `Regression testing`: used to check if an update modifies existing behavior
   - `Sanity testing`: used to check if the bugfix works
   - `Smoke testing`: used to quick check the status after a new build

## Testing Approaches

There are different testing approach depending on who is testing the software.
Sometimes, it is better to test the software by those people who knows what is
being done with the software whereas, it is better to test by some other people
sometimes to know whether people can see the solution from another angle.

### Black-box testing

Black-box testing is a software testing method where the tester evaluates the
functionality of an application without knowing the internal code, structure,
or implementation. The focus is entirely on inputs, outputs, and the expected
behavior of the software.

### White-box testing

White-box testing is a software testing method where the tester examines the
internal structure, design, or code of the application to ensure that it works
as expected. It is also known as clear-box testing, glass-box testing, or
structural testing.

### Grey-box testing

Grey-box testing is a software testing method that combines aspects of both
black-box and white-box testing. The tester has partial knowledge of the
internal workings of the software, which is used alongside functional testing
to improve test coverage and effectiveness.
