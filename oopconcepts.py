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
# Tools > Run Python console
# p1.name
# p2.name
# p1
# p2
# p2 = p1
# p1
# p2
# p1 is p2 (this will return True)
# p1.name = "Alex"
# p1.name (indeed returns the changed name)
# p2.name (will also return 'Alex')
# p2 = Person("Christopher")
# p1 (still points to the same memory location)
# p2 (now points to a different memory location, because:)
# EVERY OBJECT NEEDS A UNIQUE MEMORY LOCATION
# The memory address is like the unique id of an object, and python has a built in function that returns a decimal number that is
# the same as the hexadecimal address:
# id(p1)