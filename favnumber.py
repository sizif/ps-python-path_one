import random

print("Hello, what is your favorite number?")
number = input()

print("Your favorite number is " + str(number))

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)
print(magicNumber)