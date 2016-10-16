class Cart:

    def __init__(self):
        self._contents = dict()

    def process(self, order):
        if order.add:
            if not order.item in self._contents: # (4)
                self._contents[order.item] = 0 # (5)
            self._contents[order.item] += 1 # (6)
        elif order.delete: # (7)
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item] <= 0: # (8)
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

# (1) How to access order.add, order.delete, in cart? Currently, order doesn't expose an item so let's add an item attribute, and I'll set it to the None object
# (1i) The none object means it's not pointing to anything significant
# (2) And we'll add a self on the item string
# (3) And we'll essentially need to implement this logic from def add_to_cart, but now instead of taking an item parameter, we'll get the item from the order...
# (3) ...and instead of taking the cart parameter, we're gonna use the dict that is internal inside of the Cart, the _contents.
# (3) The 1st thing that add_to_cart did was if the item was corrently not in the cart, it would att that item with initial qty 0, and then every time we add something we increment it by 1
# (4) that logic in Cart.process would look something like this, if the item is not in the contents, add it by...
# (5) ...indexing into it, [order.item] is my key, 0 is my value
# (6) And now I'll copy that line of code, because what we need to do here, after we're sure that that item is in the cart, let's pull it out and add one to it.
# (7) And now delete is self-explanatory
# (8) Finally, check if the item is at zero in the order.delete, and if it is, remove it completely from the dictionary
