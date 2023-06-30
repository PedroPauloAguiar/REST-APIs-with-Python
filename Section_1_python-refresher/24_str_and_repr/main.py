class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    def __repr__(self):  # Mais usual para depurar o código.
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)
print(bob)
