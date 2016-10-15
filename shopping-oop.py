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

def go_shopping():
    cart = dict()

    while True:
        order = get_order()

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()

# We'll convert this program to oop concepts. When I look at this program, I see 2 broad concepts:
# A lot of logic around order, getting it, processing it...
# A lot of logic around cart.
# THE FACT THAT SO MANY METHODS HAVE A CART PARAMETER, TELLS ME WE SHOULD PROBABLY HAVE A CART OBJECT, with methods that manipulate a cart attribute that's part of the class.
# That way we don't have to pass the cart around, it's already encapsulated in the object.
# So my next step, I'll make a cart class, and maybe an order class too