[go to course contents](https://github.com/ghimiresdp/pythrone/)
<hr>

# Chapter 16: Decorators

> **Note**:
>
> please refer to the repository
> **[python projects](https://github.com/ghimiresdp/python-projects)** for more
> exercises and projects related to this chapter.

**Table of contents**:
- [Chapter 16: Decorators](#chapter-16-decorators)
- [Introduction to decorators](#introduction-to-decorators)
- [decorator factories](#decorator-factories)
- [class based decorators](#class-based-decorators)


# Introduction to decorators

Decorators are higher order functions that accept functions or callables as
arguments, modifies it's base behavior, and finally returns the same callable by
updating the arguments accordingly.

Decorator pattern is a well-known design pattern in programming language that
helps us utilizing the same feature along multiple functions without changing
each functions repeatedly.

For example, we have 2 functions, `add` and `subtract`, that can subtract only
numeric values, however if we want to be able to subtract a number string from
another, then we might first need to check if the parameters can be converted to
number or not. However, this process needs to be repeated for all the methods
like `add` and `subtract`. To avoid such repetition, we can introduce a new
decorator that checks these conditions and automatically typecast values to it.

```python
def auto_typecast(fn):
    def inner(x: str, y):
        if isinstance(x, str):
            x = int(x)
        if isinstance(y, str):
            y = int(y)
        return fn(x, y)

    return inner


@auto_typecast
def add(x, y):
    return x + y


@auto_typecast
def subtract(x, y):
    return x - y


if __name__ == "__main__":
    print("adding number 5 and string '6': ", add(5, "6"))
    print("subtracting number 5 from string '10': ", subtract("10", 5))

```

# decorator factories

# class based decorators
