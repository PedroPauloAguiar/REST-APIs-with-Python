# Example 1
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# Example 2
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)


# Example 3
def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, must be mapping
myfunction(**none)  # Error
