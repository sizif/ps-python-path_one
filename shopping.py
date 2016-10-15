def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item

def process_order(order, cart):
    command, item = order

    if command == "a":
        cart.add(item)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = set()

    while True:
        order = get_order()

        process_order(order, cart)

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()

# DICTIONARIES:
# To construct a dict, I can use a built-in function dict():
# adict = dict() constructs a new empty dictionary
# or I can create it just like a set, with {} braces, but while the set had single items,
# a dictionary holds key-value pairs:
# adict = { "scott":"@OdeToCode", "pluralsight":"@Pluralsight" }
# but I cant offset into them like this: adict[0] as this returns a KeyError
# Instead, I use the value from the key:value pair:
# adict["scott"]
# You can also iterate through a dictionary, and return keys:
# for key in adict:
#   print(key)
# And you can return values too:
# for key in adict:
#   print(adict[key]) # "give me a value for that particular key"
# Finally, I can print them both out:
# for key in adict:
#   print(key, adict[key])
# "Dear dictionary, here's a new value to store:
# adict["count"] = 4

# THE KEYS DON'T HAVE TO BE STRINGS
# They can be different types of objects.


