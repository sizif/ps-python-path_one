def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item

def process_order(order, cart):
    command, item = order

    if command == "a":
        cart.append(item)
    elif command == "d" and item in cart: # (1) let's make sure the item to be removed is in the cart!
        cart.remove(item)
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = []

    while True:
        order = get_order()

        process_order(order, cart)

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()
