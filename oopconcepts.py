# CREATE OUR OWN OBJECT
class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self)) # (3)
        print("Hello, ", self.name)

room = [] # (2)
room.append() # (3)


# (1) Combining Person and list, imagine we had to write an application for managing a classroom
# (2) So we'll have to handle multiple Person objects and group them into a specific classroom
# (3) Now I can start appending Person objects into that list