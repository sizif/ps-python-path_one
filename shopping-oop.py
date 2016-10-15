class Cart:

    def __init__(self):
        self._contents = dict()

class Order:

    def __init__(self):
        self.quit = False # (5)

    def get_input(self): # (6)
        print("[command] [item] (command is a to add, d to delete, q to quit)")
        line = input()

        command = line[:1]
        item = line[2:]

        if command == "q":
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

while not order.quit: # (1)
    # (2)
    order = Order() # (3)
    order.get_input() # (4)

# (1) now I need to loop until I'm finished processing orders, but how can I know when we are going to finish?
# (1) wouldn't it be nice if an order object exposed a quit attribute that told me when to quit, because the order will have the user's input, it will be able to parse it out and
# (1) say, 'yes, we should quit', or 'no, we shouldn't quit', so as long as that quit Boolean, that flag, is flase, we'll continue looping and accepting new orders.
# (2) and the line of code right under this, will be the code to process this order, so give the order to the cart, have it figure out what to add or remove, but I'm going to leave that out right now
# (3) and I'm trying to focus just on what should I put in an order. So we've processed an order, and now I wanna use a new instance of the order; I don't wanna reuse the old instance
# (4) and I want the order to get new input from the user, find out what the next order should be.
# (5) This is a good time to test, but before we do, we need the quit attirbute, and the get_imput() method. And this way of oop building is similar to what we had when we first built the function name and later we specified what it does. So that's very useful
# (5) So it looks like init method might be useful for the order, because one of the things I can do in here is initialize a quit attribte and initialize it to a false value.
# (5) So by default, the order won't tell us to quit. It's only if the user tells us to quit, that we will.
# (6) And we need get input, that also takes a self parameter, and we'll borrow some of our previous non-oop code. I'm not going to return anything from get_input(), all of that will be encapsulated inside the order class itself.
# (7) At this point you can test, it prompts for a command, I type q and it quits