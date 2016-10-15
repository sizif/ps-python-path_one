class Classroom:

    def __init__(self):
        self._people = []

class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self)) # (3)
        print("Hello, ", self.name)

# (1) But let's raise this to a new level of abstraction, and create sth a bit more interesting and focused on our goals
# (2) So I'll create a new class, called Classroom
# (3) the _people will be the attribute of every object that gets instantiated from this class, and I'll set it to a new empty list
# (4) the _people is a convention that shows that _people is only to be used on methods on this class, so other programmers are not
# (4) supposed to touch that variable
# (5) So I can to this: room = Classroom(); room._people = ...; but I'm not supposed to, it's sort of an agreement not to do it