# CREATE OUR OWN OBJECT
class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self)) # (3)
        print("Hello, ", self.name)

# (1) What will it print now?
p1 = Person("Scott")
p2 = Person("Alex")
print(id(p1))
print(id(p2))
p1.say_hello()