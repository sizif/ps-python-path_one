def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item

def add_to_cart(item, cart): # (4)
    if not item in cart: # (4)
        cart[item] = 0 # (4)
    cart(item) += 1 # (5)

def process_order(order, cart):
    command, item = order

    if command == "a":
        add_to_cart(item, cart) # (2)
    elif command == "d" and item in cart:
        delete_from_cart(item, cart) # (3)
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = dict() # (1)

    while True:
        order = get_order()

        process_order(order, cart)

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()

# (1) To be able to take batches of same things, we'll start by changing the cart from a set to a dictionary
# (2) There will have to be a bit more logic, so in def process_order, let's change 'cart.add(item)' to a function call, ('add_to_cart')
# (2) We'll pass it item and cart, and this function can figure out if there is sth already there and ++ it, or create a key:value pair if it's not there
# (3) Likewise, instead of just removing from the cart, we can delete_from_cart, given the item and the cart
# (4) Now lets def add_to_cart(), that takes the item and the cart, and ask it if there are "apples" in cart, which returns T or F
# (4) So if the user wants to add apples to the cart we'll do it but we'll set the initial counter to 0, and only if there's no apples there
# (5) And finally, we'll always += 1 the item