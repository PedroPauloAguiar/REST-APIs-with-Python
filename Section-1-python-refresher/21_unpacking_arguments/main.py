# example 1
# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg

#     return total


# print(multiply(1, 3, 5))


# Example 2
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provide to apply()."


print(apply(1, 3, 6, 7, operator="*"))


# Example 3
def add(x, y):
    return x + y


nums = {"x": 15, "y": 25}
print(add(**nums))
