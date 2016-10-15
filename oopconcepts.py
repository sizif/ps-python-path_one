class Classroom:

    def __init__(self):
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self): # (1)
        for person in self._people:
            person.say_hello()

class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self))
        print("Hello, ", self.name)

room = Classroom()
room.add_person(Person("Scott"))
room.add_person(Person("Poonam"))
room.add_person(Person("Paul"))

room.greet() # (2)


# (1) So far I can only add and remove people, but let's add a method that'll deal with the whole group, greet them
# (2) Alright so let's greet everybody (plus we can still see their addresses)