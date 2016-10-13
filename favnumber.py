import random

print("Hello, what is your favorite number?")
number = input()

print("Your favorite number is " + str(number))

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
    print("Guess what it is?")
    guess = input()
    if guess == magicNumber:
        found = True

    
  