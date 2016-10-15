# CREATE OUR OWN OBJECT
class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, ", self.name)

p1 = Person("Scott")
p1.say_hello()

p2 = Person("Allen")
p2.say_hello()

# Objects live in memory
# variables are pointers, or references, to the location in the memory at which the object 'lives'
# It's like trying to get a piece of information from only 1 of a million boxes; a variable can contain the number of the box that you need to look in