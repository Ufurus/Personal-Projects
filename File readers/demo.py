class Person:
    kind = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Pesho", 25)
person2 = Person("Tosho", 35)
print(person1.kind)