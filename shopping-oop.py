class Cart: # (1)

    def __init__(self):
        self._contents = dict() # (2)

class Order: # (4)



def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item

def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1

def delete_from_cart(item, cart):
    if item in cart:
        cart[item] -= 1

def process_order(order, cart):
    command, item = order

    if command == "a":
        add_to_cart(item, cart)
    elif command == "d" and item in cart:
        delete_from_cart(item, cart)
    elif command == "q":
        return False

    return True

cart = Cart() # (3)
order = Order() # (5)
order.get_input()

# (1) I'll leave most of the existing code in, but I'll rethink def go_shopping(), because instead of the cart being a dictionary, it's now an object of the cart class
# (2) that encapsulates a dictionary
# (3) I want the cart to be an instance of the shopping cart class.
# (4) And the next thing I want to do is get an order from the user, so I can put something in the cart.
# (4) And how do I want to represent an order? Well, I do see that order is used throughout the program too. So I'll add an order class definition.
# (5) Planning classes, give them a SINGLE responsibility (small, focused classes)
# (5) Another approach to OOP is "write the code that will use the class, before you write the class"
# (5) So lets write some code that will use an order, first I'll instantiate it...
# (6) ...and I'm thinking, order might be the place to get input, so I'll let user type something, so it knows what the order is