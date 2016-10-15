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
room.add_person(Person("Scott")) # (1) (2)
room.add_person(Person("Poonam")) # (3)
room.add_person(Person("Paul")) # (3)

# (1) Let's add Scott to the room
# (2) I don't need to keep a variable around to manage a pointer to that person, I'm just going to let the classroom take care of that
# (3) Let's add more people