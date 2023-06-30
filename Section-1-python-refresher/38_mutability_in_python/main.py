a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

print(id(a))
print(id(b))
