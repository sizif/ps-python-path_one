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
    elif command == "d":
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

# (1) At this point, the code works, but we get a runtime error if we try to delete something that's not in the list
