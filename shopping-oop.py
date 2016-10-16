class Cart:

    def __init__(self):
        self._contents = dict()

    def process(self, order): # (1)
        if order.add: # (4)


class Order:

    def __init__(self):
        self.quit = False
        self.add = False # (2)
        self.delete = False # (2)

    def get_input(self):
        print("[command] [item] (command is a to add, d to delete, q to quit)")
        line = input()

        command = line[:1]
        item = line[2:]

        if command == "a": # (4)
            self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True

def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1

def delete_from_cart(item, cart):
    if item in cart:
        cart[item] -= 1

def process_order(order, cart):
    command, item = order

    if command == "a": # (3)
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

# (i) take the order and figure out if the user wants to add something or delete something
# (1) now let's define cart.process(), it takes a self param by default, but I'll also have to pass it the order
# (2) now inside cart.process() def, I need to check if the order is an add or a delete
# (2) and once again, this might be useful if we just exposed attributes from the order itself, that tells us if an order is an 'a' or a 'd'
# (2) because it would be much nicer to do those string comparisons inside of class Order where we know the user's input, instead of trying to expose things from class Order, like 'command' exposed just as a string
# (2) so let's add a few more attributes, and say, by default this is not an add order, and it's not a delete order...
# (3) ... but once we have the input from the user we will figure out if it is an add or a delete ( in class Order > def get_input )
# (4) finally, with the abstraction of command checking in class Order, class Cart can benefit from this abstraction, I can say if order.add: