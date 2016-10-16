class Cart:

    def __init__(self):
        self._contents = dict()

    def __repr__(self): # (1)
        return "{0} {1}".format(Cart, self.__dict__) # (2) and # (3)


    def process(self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item] <= 0:
                    del self._contents[order.item]


class Order:

    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None # (1)

    def get_input(self):
        print("[command] [item] (command is a to add, d to delete, q to quit)")
        line = input()

        command = line[:1]
        self.item = line[2:] # (2)

        if command == "a":
            self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True

def add_to_cart(item, cart):
    if not item in cart: # (3)
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

cart = Cart()
order = Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = Order()
    order.get_input()

# (1) let's display the cart contents to the user using special attributes and special methods in a python object (e.g. __init__), namely __repr__, by overriding its behavior
# (2) in python, you can convert almost anything to a string (that's the return "*" bit)
# (3) we'l use __dict__ here, because with it, you can dump out everything that is inside of an object, including exposed and hidden ones
# (3) so we can test __dict__ byt exposing order ( order.__dict__) - this is literally a dictionary tath is returned, so I can index into it and I'll try to get the value for the key "quit"
# (3) ...like this: order.__dict__["quit"], and right now it will tell me that that value is true. So it might be useful when producing this representation just to dump it out, like this:
# (3) self.__dict__
