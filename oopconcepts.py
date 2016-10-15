# CREATE OUR OWN OBJECT
class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self)) # (3)
        print("Hello, ", self.name)

# (1) Will p1.say_hello() print out, Scott or Alex
p1 = Person("Scott")
p2 = p1
p2.name = "Alex"
p1.say_hello()

# (2) we'll verify the result by priting the id's for both objects
print(id(p1))
print(id(p2))
