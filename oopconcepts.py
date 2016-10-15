class Classroom:

    def __init__(self):
        self._people = []

    def add_person(self, person): # (1)
        self._people.append(person) # (2)

    def remove_person(self, person):
        self._people.remove(person) # (3)


class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self)) # (3)
        print("Hello, ", self.name)

room = Classroom()

# (1) let me def add_person, that takes the self parameter, and a person object
# (2) and when it get's invoked, we will walk up to the people list and we will append that person.
# (3) let's also remove someone from the classroom
# (4) And now I can use my room